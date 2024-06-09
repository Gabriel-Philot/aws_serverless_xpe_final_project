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

    
args = getResolvedOptions(sys.argv, ["JOB_NAME", "bucketname", "stockapipath", "refinedstockapi"])
spark = create_spark_session()
sc = spark.sparkContext
glueContext = GlueContext(sc)
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


# --------------  VAR FIXAS -----------------
BUCKET = args['bucketname'] 


## ------------------ MOBILE VARS [NEED TO BE CHANGED] ------------------
stockapipath = args['stockapipath']
refinedstockapi = args['refinedstockapi']

######################################################################################
                                    # Stock api
######################################################################################

# Read
df_trusted_data = spark.read \
    .format("delta") \
    .load(f"s3://{BUCKET}/{stockapipath}")

cols_stocks_api = [
    "regularMarketPrice",
    "regularMarketChangePercent",
    "regularMarketVolume",
    "averageDailyVolume10Day",
    "averageDailyVolume3Month",
    "currency",
    "fiftyTwoWeekHigh",
    "fiftyTwoWeekLow",
    "longName",
    "shortName",
    "symbol",
    "twoHundredDayAverage",
    "twoHundredDayAverageChange",
    "twoHundredDayAverageChangePercent",
    "date_ingestion",
    "dateingestion_sp",
    "processing_date"
]

df_stocks_select = df_trusted_data.select(cols_stocks_api)

# calc Daily return

df_tra = df_stocks_select \
    .withColumn(
    "data_col_calc", date_format("dateingestion_sp", "yyyy-MM-dd")
    )

windowSpec = Window.partitionBy("symbol").orderBy("dateingestion_sp")

df_tra = df_tra \
    .withColumn("previous_price", lag("regularMarketPrice").over(windowSpec)) \
    .withColumn("daily_return",
        round(
            when(col("previous_price").isNotNull(), 
                    (col("regularMarketPrice") - col("previous_price")) / col("previous_price") * 100)
                    .otherwise(None), 
            3)
               ) \
    .drop("previous_price" , "date_col_cal")

# save

df_tra.coalesce(1).write \
    .format("delta") \
    .mode("append") \
    .save(f"s3://{BUCKET}/{refinedstockapi}")

######################################################################################
                            # Delta + Catalog Table
######################################################################################

base_s3_path = f"s3://{BUCKET}"
final_base_path = f"s3://{BUCKET}/{refinedstockapi}"
table_name = "refined-stock-api"
final_base_path = f"s3://{BUCKET}/{refinedstockapi}".format(
    base_s3_path=base_s3_path, table_name=table_name
)

delta_df = DeltaTable.forPath(spark, final_base_path)
delta_df.generate("symlink_format_manifest")

print("*********** OK ************")

job.commit()






