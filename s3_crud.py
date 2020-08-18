import boto3
from config import get_bucket_name,get_bucket,get_s3_resource
from botocore.exceptions import ClientError
from pathlib import PureWindowsPath,Path
from boto3.s3.transfer import TransferConfig


def get_all_objects():
    bucket = get_bucket()
    print(f'Bucket name:{bucket}')
    objects = bucket.objects.all()
    for object in objects:
        print(object)



def upload_file(file):
    my_bucket = get_bucket()
    my_bucket.Object(file.filename).put(Body=file)


def get_s3_url(filename):
    '''Returns URL of for the file in S3 bucket'''
    if filename != "":
        bucket =get_bucket_name()
        s3_url = f"https://{bucket}.s3.us-east-2.amazonaws.com/{filename}"
        print(f"s3_url: {s3_url}")
        return  s3_url
    else:
        return ""

