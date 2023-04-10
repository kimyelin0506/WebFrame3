from django.contrib import admin
from django.urls import path, include
from . import views #. = 현재 위치에 있는 view파일 가져오기
urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]
