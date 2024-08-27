from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

class UserAccount(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    verified = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, unique=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    picture = ResizedImageField(size=[600, 600], quality=85 ,upload_to='profiles', blank=True, null=True)
    bio = models.TextField(max_length=800, null=True, blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email.strip('@')
