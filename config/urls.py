from django.contrib import admin
from django.urls import path, include

import aptcomplex.views
from board import views as board_views
from aptcomplex import views


urlpatterns = [
    path("", aptcomplex.views.index),
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("board/", include("board.urls")),
]
