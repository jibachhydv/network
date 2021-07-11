from django.contrib import admin

from postapp.models import Post, Comment, LikeModel

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikeModel)
