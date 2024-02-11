from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True,default='')
    profileimg = models.ImageField(upload_to='profileimg', default='blank-profile-picture.png')
    location = models.CharField(max_length=100,blank=True, default='')

    def __str__(self):
        return self.user.username

class Feature(models.Model):
    name = models.CharField(max_length=123)
    details = models.CharField(max_length=123)

class Post(models.Model):
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")
    title = models.CharField(max_length=123)
    image = models.ImageField(upload_to='post_image', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class View(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.views)

class Comment(models.Model):
    date = models.DateField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

