from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from knox import views as knox_views
from .views import LoginView, RegisterUserView, ChangepasswordView

app_name = "main"

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='knox_login'),
    path('accounts/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/Changepassword/', ChangepasswordView.as_view(), name='Changepassword'),
    path('accounts/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]
