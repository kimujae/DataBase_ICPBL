from django.contrib import admin
from django.urls import path
from . import  views



app_name = 'maintenence'

urlpatterns = [
    path('', views.index_1,name ="index"),
    path('detail', views.detail_1, name="detail"),
]
