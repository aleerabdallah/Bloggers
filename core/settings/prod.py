from .common import *
from django.conf.global_settings import DATABASES
import dj_database_url

# DATABASE

DATABASES['default'] = dj_database_url.parse(
    os.getenv('DB_URL'),
    conn_max_age=600

)

# Production CHECKLIST

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}


STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# Static Files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

