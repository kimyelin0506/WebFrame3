from django.contrib import admin
from .models import Post #현재 경로 .에 있는 Post 가져오기

# Register your models here.
admin.site.register(Post)
