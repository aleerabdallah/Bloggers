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



STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}




STATIC_URL = '/static/'
MEDIA_URL = '/media/' 


# STATIC Files

STATIC_ROOT = os.path.join(BASE_DIR, 'Tech')


# MEDIA FIles
MEDIA_ROOT = os.path.join(BASE_DIR, "Techbros/")

