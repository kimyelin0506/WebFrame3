from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
]
#<type:변수명> :url에 입력