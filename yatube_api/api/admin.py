from django.contrib import admin
from posts.models import Post, Group, Comment

# Самая простая регистрация:
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
