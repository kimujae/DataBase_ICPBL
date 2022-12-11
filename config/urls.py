from django.contrib import admin
from django.urls import path, include

import aptcomplex.views
from board import views as board_views
from aptcomplex import views
from maintenence import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", aptcomplex.views.index),
    path("aptcomplex/", include("aptcomplex.urls")),
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("board/", include("board.urls")),
    path("maintenence/", include('maintenence.urls')),
    path("reservation/",include('reservation.urls')),
    path("parking/", include('parking.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)