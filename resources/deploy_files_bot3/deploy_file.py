import boto3
from botocore.exceptions import ClientError

def upload_file(file_path, PREFIX, BUCKET, file_name_and_type, PROFILE):
    s3= boto3.Session(profile_name=PROFILE).resource('s3')
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(name= BUCKET)

    key = f"{PREFIX}/{file_name_and_type}"
    s3_bucket.put_object(
    Body=file_path,
    Key=key
    )
    
    return f"\ns3://{BUCKET}/{key}"


