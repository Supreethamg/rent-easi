import logging
import boto3
from botocore.exceptions import ClientError


import os

S3_BUCKET = os.environ.get("AWS_S3_BUCKET")
S3_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
S3_SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY")
S3_REGION = os.environ.get("AWS_DEFAULT_REGION")

# Retrieve the list of existing buckets
def get_s3_resource():
    if S3_KEY and S3_SECRET:
        return boto3.resource(
            's3',
            aws_access_key_id=S3_KEY,
            aws_secret_access_key=S3_SECRET
        )
    else:
        return boto3.resource('s3')


def get_bucket():
     
    # if 'bucket' in session:
    #     bucket = session['bucket']
    # else:
    #     bucket = S3_BUCKET

    return get_s3_resource().Bucket(S3_BUCKET)


def get_buckets_list():
    client = boto3.client('s3')
    return client.list_buckets().get('Buckets')