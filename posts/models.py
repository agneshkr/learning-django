from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)   #@! check if this works.
    body=models.TextField(max_length=2000)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="posts_written")

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


