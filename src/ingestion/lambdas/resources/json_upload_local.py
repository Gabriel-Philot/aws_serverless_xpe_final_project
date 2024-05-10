import boto3 # rite_json_to_s3
from io import BytesIO
import json

def write_json_to_s3(json_data, bucket_name, prefix, date, Prof_name):

    # Get ingestion date
    ingestion_date = date

    # Define S3 path with partitioning 
    s3_path = f"{prefix}{ingestion_date.strftime('%Y%m%d')}/file.json"


    json_string = json.dumps(json_data)

    # Get size of JSON buffer
    json_bytes = json_string.encode('utf-8')
    json_buffer = BytesIO(json_bytes)
    json_size = json_buffer.getbuffer().nbytes

    # Write JSON buffer to S3
    s3 = boto3.Session(profile_name=Prof_name).resource('s3')
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(name= bucket_name)

    s3_bucket.put_object(
    Body=json_string,
    Key=s3_path  
    )

    return f"s3://{bucket_name}/{s3_path}", json_size