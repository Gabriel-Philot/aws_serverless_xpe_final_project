######################################################################################
                                    # IMPORTS #
######################################################################################


try:
    import os
    import sys
    import uuid

    import pyspark
    from pyspark import SparkConf, SparkContext
    from awsglue.job import Job
    from pyspark.sql import SparkSession
    from pyspark.sql.window import Window
    from pyspark.sql.functions import row_number, col, desc, lag, when
    from pyspark.sql.functions import col, asc, desc, current_timestamp, lit
    from awsglue.utils import getResolvedOptions
    from awsglue.dynamicframe import DynamicFrame
    from awsglue.context import GlueContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import StructType, StructField, StringType, BooleanType, FloatType, LongType, DoubleType, DateType, IntegerType, DecimalType
    import time
    import csv
    import boto3
    from datetime import datetime, timedelta
    from delta.tables import *

    print("All modules are loaded .....")

except Exception as e:
    print("Some modules are missing {} ".format(e))
    
    
def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()
    return spark

######################################################################################
######################################################################################

    
args = getResolvedOptions(sys.argv, ["JOB_NAME", "bucketname", "divipath", "histpath", "refineddivhist"])
spark = create_spark_session()
sc = spark.sparkContext
glueContext = GlueContext(sc)
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


# --------------  VAR FIXAS -----------------
BUCKET = args['bucketname'] 


## ------------------ MOBILE VARS [NEED TO BE CHANGED] ------------------
dividends_migration_path = args['divipath']
historical_migration_path = args['histpath']
divhistrefinedpath = args['refineddivhist']

######################################################################################
                                    # Div+hist
######################################################################################

# Div data
schema = StructType([
    StructField('approvedon', StringType(), True),
    StructField('symbol', StringType(), True),
    StructField('assetissued', StringType(), True),
    StructField('isincode', StringType(), True),
    StructField('label', StringType(), True),
    StructField('lastdateprior', StringType(), True),
    StructField('paymentdate', StringType(), True),
    StructField('rate', FloatType(), True),
    StructField('relatedto', StringType(), True),
    StructField('remarks', StringType(), True),
    StructField('update_key', StringType(), True)
])

dividends_data = spark.read \
    .format("csv") \
    .option("header", "false") \
    .schema(schema) \
    .load(f"s3://{BUCKET}/{dividends_migration_path}")
    
cols_select = ["symbol", "rate", "paymentdate"]


dividends_data_select = dividends_data.select(*cols_select) \
    .withColumn("paymentdate", date_format("paymentdate", "yyyy-MM-dd"))

# Hist data

new_schema = StructType([
    StructField('date', StringType(), True),
    StructField('open', FloatType(), True),
    StructField('high', FloatType(), True),
    StructField('low', FloatType(), True),
    StructField('close', FloatType(), True),
    StructField('volume', IntegerType(), True),
    StructField('adjustedclose', FloatType(), True),
    StructField('symbol', StringType(), True),
    StructField('update_key', StringType(), True)
])

stock_hist = spark.read \
    .format("csv") \
    .option("header", "false") \
    .schema(new_schema) \
    .load(f"s3://{BUCKET}/{historical_migration_path}")


cols_select_hist = ["date", "symbol", "close", "adjustedclose", "volume"]
stock_hist_select = stock_hist.select(*cols_select_hist)


# Join

dividends_data_select = dividends_data_select.withColumnRenamed('symbol', 'dividend_symbol')

join_hist_div = stock_hist_select.join(
    dividends_data_select,
    (stock_hist_select['symbol'] == dividends_data_select['dividend_symbol']) & 
    (stock_hist_select['date'] == dividends_data_select['paymentdate']),
    how='left'
).drop('dividend_symbol') \
    .where(col("date") >= "2023-12-18") # first match date just for the sake off this poc.
    
# Here the goal its to get the last dividend payment cols and replicate it until the next value

window_spec = Window.partitionBy('symbol').orderBy('date').rowsBetween(Window.unboundedPreceding, Window.currentRow)

window_hist_div = join_hist_div \
    .withColumn('last_dividend_date', last('paymentdate', ignorenulls=True).over(window_spec)) \
    .withColumn('last_dividend_rate', last('rate', ignorenulls=True).over(window_spec)) \
    .drop('rate', "paymentdate")
    
window_hist_div.coalesce(1).write \
    .format("delta") \
    .mode("overwrite") \
    .save(f"s3://{BUCKET}/{divhistrefinedpath}")

######################################################################################
                            # Delta + Catalog Table
######################################################################################

base_s3_path = f"s3://{BUCKET}"
final_base_path = f"s3://{BUCKET}/{divhistrefinedpath}"
table_name = "refined-div-hist"
final_base_path = f"s3://{BUCKET}/{divhistrefinedpath}".format(
    base_s3_path=base_s3_path, table_name=table_name
)

delta_df = DeltaTable.forPath(spark, final_base_path)
delta_df.generate("symlink_format_manifest")

print("*********** OK ************")

job.commit()






