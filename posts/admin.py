from django.contrib import admin

from posts.models import Post, Rating

admin.site.register(Post)
admin.site.register(Rating)
