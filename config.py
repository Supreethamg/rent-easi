import logging
import boto3
from botocore.exceptions import ClientError
import os

S3_BUCKET = os.environ.get("AWS_S3_BUCKET")
S3_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
S3_SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY")
S3_REGION = os.environ.get("AWS_DEFAULT_REGION")
SMTP_USERNAME = os.environ.get("AWS_SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("AWS_SMTP_PASSWORD")
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

def get_bucket_name():
    '''Returns s3 bucket name'''
    return S3_BUCKET

def get_region():
    '''Returns s3 bucket name'''
    return S3_REGION

def get_smtp_username():
    '''Returns smtp user name'''
    return SMTP_USERNAME

def get_smtp_password():
    '''Returns smtp password'''
    return SMTP_PASSWORD

def get_bucket():
    ''' returns s3 bucket object'''
    return get_s3_resource().Bucket(S3_BUCKET)


