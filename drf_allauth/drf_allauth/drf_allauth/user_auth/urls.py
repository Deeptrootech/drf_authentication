from allauth.account.views import ConfirmEmailView, confirm_email
from dj_rest_auth.jwt_auth import get_refresh_view
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordResetView, PasswordResetConfirmView, \
    PasswordChangeView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import FacebookLogin

app_name = "user_auth"

urlpatterns = [

    # 1) from dj-rest-auth/urls.py # import dj_rest_auth.urls
    # path('', include('dj_rest_auth.urls')),

    # # or define it here and include related views from dj-rest-auth/views.py
    # # incase if you need to customize their views
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password/reset/', PasswordResetView.as_view()),
    path('password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('user/', UserDetailsView.as_view()),  # Get all users

    # If JWT is  used then token/verify and token/refresh will also be included.
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),

    # 2) from dj-rest-auth/registration/urls.py (Problems in registration)
    path('registration/', include('dj_rest_auth.registration.urls')),

    # # or define it here and include related views from dj-rest-auth/views.py
    # path('registration/', RegisterView.as_view()),
    # path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    # path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),

    # 3) social media
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
]
