import boto3
import os
import io
from botocore.client import Config
from dotenv import load_dotenv

load_dotenv()

import boto3

url = os.environ.get("S3_ENDPOINT")
key_id = os.environ.get("S3_KEY_ID")
access_key = os.environ.get("S3_SECRET")
bucket_name = os.environ.get("R2_BUCKET_NAME")

upload_object = "2025_06_03_15_52_58.png"

s3 = boto3.client(
    service_name ="s3",
    endpoint_url = url,
    aws_access_key_id = key_id,
    aws_secret_access_key = access_key,
    region_name="apac"
)
try:
    with open(upload_object, "rb") as f:
        image_bytes = f.read()

    s3.upload_fileobj(
        io.BytesIO(image_bytes),
        bucket_name,
        upload_object,
        ExtraArgs={
            'ContentType': 'image/png'
        }
    )

    print("Success!")

except Exception as e:
    print(e)
