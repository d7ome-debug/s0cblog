from django.contrib import admin
from .models import Feature, Post, Comment, View, likes
admin.site.register(Feature)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(likes)
