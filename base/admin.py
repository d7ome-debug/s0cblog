from django.contrib import admin
from .models import *
admin.site.register(Feature)
admin.site.register(Comment)
admin.site.register(View)
admin.site.register(Profile)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    resource_class = Post


    jazzmin_section_order = ("title", "date", "author")