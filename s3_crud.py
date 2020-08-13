import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET,S3_REGION,get_bucket,get_s3_resource
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


