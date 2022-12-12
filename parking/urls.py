from django.urls import path
from . import views

app_name = 'parking'

urlpatterns = [
    path('1/', views.parking1, name="parking1"),
    path('2/', views.parking2, name="parking2"),
    path('3/', views.parking3, name="parking3"),
    path('inquiry/', views.inquiry, name="inquiry"),
]