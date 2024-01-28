from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image" ] # something like this
        
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profileimg", "location" ] # something like this


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]