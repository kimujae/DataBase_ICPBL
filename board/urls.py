from django.contrib import admin
from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path("board_list_dong/<str:category_name>", views.board_list_dong, name="board_list_dong"),
    path("board_list_complaint/<str:category_name>", views.board_list_complaint, name="board_list_complaint"),
    path("board_create/", views.board_create, name="board_create"),
    path("board_read/<int:board_id>", views.board_read, name="board_read"),
    path("board_update/<int:board_id>", views.board_update, name="board_update"),
    path("board_delete/<int:board_id>", views.board_delete, name="board_delete"),
    path("reply_create/<int:board_id>", views.reply_create, name="reply_create"),
    path("reply_update/<int:board_id>/<int:reply_id>", views.reply_update, name="reply_update"),
    path("reply_delete/<int:board_id>/<int:reply_id>", views.reply_delete, name="reply_delete"),
]
