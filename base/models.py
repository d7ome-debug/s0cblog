from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=123)
    details = models.CharField(max_length=123)

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='post_image', default='https://th.bing.com/th/id/R.cfcea7bab839544cbd50bad837242ed3?rik=i38TTljz3p%2foig&pid=ImgRaw&r=0')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title