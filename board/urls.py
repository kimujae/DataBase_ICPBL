from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'board'

urlpatterns = [
    path("board_list_dong/<str:category_name>", views.board_list_dong, name="board_list_dong"),
    path("board_list_complaint/<str:category_name>", views.board_list_complaint, name="board_list_complaint"),
    path("board_list_joonggo/<str:category_name>", views.board_list_joonggo, name="board_list_joonggo"),
    path("board_list_bunsil/<str:category_name>", views.board_list_bunsil, name="board_list_bunsil"),
    path("board_create_notice/", views.board_create, name="board_create_notice"),
    path("board_create_minwon/", views.board_create_minwon, name = "board_create_minwon"),
    path("board_create_joonggo/", views.board_create_joonggo, name = "board_create_joonggo"),
    path("board_create_bunsil/", views.board_create_bunsil, name = "board_create_bunsil"),
    path("board_read/<int:board_id>", views.board_read, name="board_read"),
    path("board_update/<int:board_id>", views.board_update, name="board_update"),
    path("board_delete/<int:board_id>", views.board_delete, name="board_delete"),
    path("reply_create/<int:board_id>", views.reply_create, name="reply_create"),
    path("reply_update/<int:board_id>/<int:reply_id>", views.reply_update, name="reply_update"),
    path("reply_delete/<int:board_id>/<int:reply_id>", views.reply_delete, name="reply_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
