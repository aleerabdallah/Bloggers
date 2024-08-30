import os 
from dotenv import load_dotenv
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


load_dotenv()




# AWS_PUBLIC_LOCATION = 'public'
# AWS_PRIVATE_LOCATION = 'private'





class PublicMediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get("AWS_PUBLIC_STORAGE_BUCKET_NAME")
    file_overwrite = False 



class PrivateMediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get("AWS_PRIVATE_STORAGE_BUCKET_NAME")
    file_overwrite = False 

