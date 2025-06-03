from auto import apiLoad, graph
from storage import uploadR2
from dotenv import load_dotenv
import os
import boto3
from botocore.client import Config
from datetime import datetime

load_dotenv()

## Graph Creation
api_key = os.environ.get('API_KEY')
data = apiLoad(api_key)
graph_bytes = graph(data)

date_filename = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

## R2 Upload
url = os.environ.get("S3_ENDPOINT")
key_id = os.environ.get("S3_KEY_ID")
access_key = os.environ.get("S3_SECRET")
bucket_name = os.environ.get("R2_BUCKET_NAME")

s3 = boto3.client(
    service_name ="s3",
    endpoint_url = url,
    aws_access_key_id = key_id,
    aws_secret_access_key = access_key,
    region_name="apac"
)

uploadR2(s3, bucket_name, date_filename, graph_bytes)