from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def follower_choices():
    pass

class Tweet(models.Model):
    title = models.CharField(max_length=200)
    twitter_post_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True,default='')
    profileimg = models.ImageField(upload_to='profileimg', default='blank-profile-picture.png')
    followers = models.ManyToManyField('self', blank=True, related_name='base_followers', symmetrical=False)
    followings = models.ManyToManyField('self', blank=True, related_name='base_followings', symmetrical=False)
    
    
    def save(self, *args, **kwargs): # args for posentinal argements kwargs for keyword posentianl argemnets
        super().save(*args, **kwargs)
        for user in self.followers.all():
            user.followings.add(self)
        for user in self.followings.all():
            user.followers.add(self)
        super().save(*args, **kwargs)
        
    
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

