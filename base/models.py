from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=123)
    details = models.CharField(max_length=123)

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='post_image', blank=True, null=True)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title