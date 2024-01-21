from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image" ] # something like this


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]