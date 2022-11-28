from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('profile_view', views.profile_view, name='profile_view'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('password_edit', views.password_edit, name='password_edit'),
]
