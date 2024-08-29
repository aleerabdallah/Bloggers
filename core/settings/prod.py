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


STATIC_URL = '/staticfiles/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# STATIC_ROOT = 'staticfiles/'

MEDIA_URL = '/userupload/' 
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE['PREFIX'] = MEDIA_URL

