from io import BytesIO
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from core.settings.storage_backends import PrivateMediaStorage
from django.conf import global_settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from PIL import Image
from django.core.files.storage import Storage
from core.settings.common import DEBUG




if DEBUG:
    storage = None
    
else:
    storage = PrivateMediaStorage()


def compress(image):    
    im = Image.open(image)   
    im_io = BytesIO()     
    im.save(im_io, im.format, quality=80)     
    new_image = File(im_io, name=image.name)    
    return new_image



class UserAccount(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    verified = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, unique=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    picture = models.ImageField(storage=storage,upload_to='Techbros/Avatar', blank=True, null=True)
    bio = models.TextField(max_length=800, null=True, blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email.strip('@')
    
    def save(self, *args, **kwargs):
        if not self.picture:
            self.picture = None
        else:
            compressed_image = compress(self.picture)
            self.picture = compressed_image
        super().save(*args, **kwargs)

