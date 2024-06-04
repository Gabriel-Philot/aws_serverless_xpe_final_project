from io import StringIO
from dotenv import load_dotenv
import os
import boto3
import pandas as pd

load_dotenv()

# Obter as variáveis de ambiente
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')
aws_bucket = os.getenv("AWS_BUCKET")
path_lambda = os.getenv("PATH_LAMBDA")
path_glue = os.getenv("PATH_GLUE")

# Configurar o boto3 com as variáveis de ambiente
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Função para baixar arquivos do S3 e armazenar em um DataFrame
def download_file_to_dataframe(bucket_name, path):
    obj = s3.get_object(Bucket=bucket_name, Key=path)
    data = obj['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(data))  # Assuming CSV format
    return df

