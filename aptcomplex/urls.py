from django.urls import path
from . import views


app_name = 'aptcomplex'

urlpatterns = [
    path("", views.index, name="index"),
    ]