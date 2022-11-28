from django.contrib import admin
from django.urls import path, include
from board import views as board_views 


urlpatterns = [
    path("", board_views.board_list),
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("board/", include("board.urls")),
]
