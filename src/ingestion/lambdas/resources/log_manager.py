import pandas as pd
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import io

class S3LogManager:
    def __init__(self, bucket_name, log_prefix, error_message):
        self.bucket_name = bucket_name
        self.log_prefix = log_prefix
        self.error_message = error_message
        self.s3_client = boto3.client('s3')
        self.log_file_name = f"scrapper_logs_{datetime.now().strftime('%Y-%m')}.csv"
        self.s3_key = f"{self.bucket_name}/{self.log_prefix}/{self.log_file_name}"

    def download_log_file(self):
        try:
            # Baixar o arquivo CSV do S3
            csv_obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=f"{self.log_prefix}/{self.log_file_name}")
            logs_df = pd.read_csv(csv_obj['Body'])
            return logs_df
        except self.s3_client.exceptions.NoSuchKey:
            # Criar um novo DataFrame vazio se não existir
            return pd.DataFrame(columns=['timestamp', 'name_fun', 'success', 'time', 'error', 'file_size'])
        except ClientError as e:
            print(f"Erro ao baixar o arquivo de log do S3: {e}")
            raise e

    def upload_log_file(self, logs_df):
        try:
            # Converter o DataFrame para um objeto de bytes
            csv_bytes = logs_df.to_csv(index=False, header=True).encode('utf-8')

            # Fazer upload do objeto de bytes para o S3
            self.s3_client.put_object(Bucket=self.bucket_name, Key=f"{self.log_prefix}/{self.log_file_name}", Body=csv_bytes)
        except ClientError as e:
            print(f"Erro ao fazer upload do arquivo de log para o S3: {e}")
            raise e

    def add_log_entry(self, name, success, time, error_message, file_size=None):
        # Baixar o arquivo CSV do S3 (ou criar um novo DataFrame vazio)
        logs_df = self.download_log_file()

        # Converter o tamanho do arquivo de megabytes para bytes
        file_size_mb = round((file_size / (1024 * 1024)), 3) if file_size is not None else None
        file_size_mb = str(file_size_mb)+" mb"

        # Adicionar uma nova entrada de log
        new_log = pd.DataFrame({
            'timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            'name_fun': name,
            'success': success,
            'time': f"{time:.2f}",
            'error': error_message,
            'file_size': [file_size_mb] 
        })
        logs_df = pd.concat([logs_df, new_log], ignore_index=True)

        # Fazer upload do DataFrame atualizado para o S3
        self.upload_log_file(logs_df)

# Exemplo de uso
# LOG_PREFIX = "l..../month={date}"
# log_manager = S3LogManager('seu-bucket', LOG_PREFIX, 'scrapper_logs.csv', date='2023-05')
# log_manager.add_log_entry('function_name', 'success', 10.25, None, 1024)