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
    from pyspark.sql.functions import col, asc, desc
    from awsglue.utils import getResolvedOptions
    from awsglue.dynamicframe import DynamicFrame
    from awsglue.context import GlueContext
    from pyspark.sql.functions import *
    import time
    import csv
    import boto3
    from datetime import datetime
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

def add_log_entry(name, success, time, bucket, log_prefix, year, month):
    # Criar uma nova entrada de log
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    success_str = str(success)
    new_log = [timestamp, name, success_str, str(time)]

    # Criar um cliente S3
    s3 = boto3.client('s3')

    # Construir o caminho completo do arquivo CSV no S3
    key = f"{log_prefix}/scrapper_glue_{year}-{month}.csv"

    try:
        # Baixar o arquivo CSV existente do S3
        obj = s3.get_object(Bucket=bucket, Key=key)
        body = obj['Body'].read().decode('utf-8').splitlines()
        rows = [row.split(',') for row in body]
    except s3.exceptions.NoSuchKey:
        # Se o arquivo não existir, criar um novo com o cabeçalho
        rows = [['timestamp', 'name_fun', 'success', 'time']]

    # Adicionar a nova entrada de log ao final do arquivo
    rows.append(new_log)

    # Converter as linhas de volta para strings CSV
    csv_data = '\n'.join([','.join(row) for row in rows])

    # Fazer upload do arquivo CSV atualizado para o S3
    s3.put_object(Body=csv_data.encode('utf-8'), Bucket=bucket, Key=key)

######################################################################################
######################################################################################
    
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
spark = create_spark_session()
sc = spark.sparkContext
glueContext = GlueContext(sc)
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


# --------------  VAR FIXAS -----------------
BUCKET = "" 


LOG_PREFIX = "dev/logs"
sucess_var = "sucess"
inicio = time.perf_counter()

## ------------------ MOBILE VARS [NEED TO BE CHANGED] ------------------
RAW_PREFIX = ""
TRUSTED_PREFIX = ""


GLUE_NAME = "brapi_crypto_raw"

######################################################################################
######################################################################################



df_bronze_data = spark.read \
            .format("json") \
            .load(f"s3://{BUCKET}/{RAW_PREFIX}")



df_silver_raw_data = df_bronze_data \
    .withColumn("processing_date", current_timestamp()) \
    .write.format("delta") \
    .mode("overwrite") \
    .save(f"s3://{BUCKET}/{TRUSTED_PREFIX}")
     

######################################################################################
######################################################################################


fim = time.perf_counter()
duration = (fim - inicio)
time_var = "{:.2f}".format(duration)
year = str(datetime.now().strftime('%Y'))
month = str(datetime.now().strftime('%m'))   

add_log_entry(GLUE_NAME, sucess_var, time_var, BUCKET, LOG_PREFIX , year, month)
print("*********** OK ************")

job.commit()