import os
import boto3
from dotenv import load_dotenv

load_dotenv('.env')

os.getenv('AWS_ACCESS_KEY_ID')
os.getenv('AWS_SECRET_ACCESS_KEY')

s3_client = boto3.client('s3')

s3_client.create_bucket(
    Bucket='my-test-s3-bucket-from-boto3-pareiko',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    }
)

response = s3_client.list_buckets()

print(response)

for bucket in response["Buckets"]:
    print(bucket)
    print(f"BUCKET NAME: {bucket['Name']}")
