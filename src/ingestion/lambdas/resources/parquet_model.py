import pyarrow as pa
import pyarrow.parquet as pq
import boto3
import sys
import io
import pandas as pd

def write_parquet_to_s3_raw(df, bucket_name, prefix, date_col):
    """
    Writes a Pandas DataFrame as a Parquet file to Amazon S3.

    Args:
        df (pandas.DataFrame): DataFrame to be written.
        bucket_name (str): Name of the S3 bucket.
        prefix (str): Prefix for the file path in the bucket.
        date_col (str): Name of the date column for ingestion date.
        partition_cols (list, optional): List of columns to partition the data.

    Returns:
        str: Full path of the Parquet file in S3.
    """
    # Convert the Pandas DataFrame to a PyArrow table
    table = pa.Table.from_pandas(df)

    # Get the ingestion date from the specified date column
    ingestion_date = pd.to_datetime(df[date_col].max())

    # Define the file path in S3 with partitioning by year, month, and day
    #year, month, day = ingestion_date.year, ingestion_date.month, ingestion_date.day
    s3_path = f"{prefix}{ingestion_date.strftime('%Y%m%d')}/file.parquet"


    # Convert the PyArrow table to a Parquet buffer
    parquet_buffer = io.BytesIO()
    pq.write_table(table, parquet_buffer, compression='snappy')

    # Get the size of the Parquet buffer
    parquet_buffer_size = parquet_buffer.tell()

    # Write the Parquet buffer to S3
    s3_resource = boto3.resource("s3")
    s3_resource.Object(bucket_name, s3_path).put(Body=parquet_buffer.getvalue())

    return f"s3://{bucket_name}/{s3_path}", parquet_buffer_size