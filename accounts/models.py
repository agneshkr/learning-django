from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# check out ->> https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
class CustomUser(AbstractUser):
    name=models.CharField(max_length=100,null=True,blank=True)
    
