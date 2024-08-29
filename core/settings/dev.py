from .common import *





INSTALLED_APPS += [
    'debug_toolbar',
]




# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# GMAIL_HOST = smtp.gmail.com
# GMAIL_HOST_USER= juniorab444@gmail.com
# GMAIL_HOST_PASSWORD= vapouwanoenrpblv

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_PORT = 587
EMAIL_HOST = os.environ.get("DEV_EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("DEV_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("DEV_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USER_SSL = False



DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

STATIC_URL = '/static/'



STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles'
]


