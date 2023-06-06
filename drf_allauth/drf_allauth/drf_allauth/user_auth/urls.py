from allauth.account.views import ConfirmEmailView, confirm_email
from dj_rest_auth.jwt_auth import get_refresh_view
from django.urls import path, include, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordResetView, PasswordResetConfirmView, \
    PasswordChangeView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import FacebookLogin, GoogleLoginView

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
    path("google/", GoogleLoginView.as_view(), name="google_login")
    # Reference:
    # https://www.rootstrap.com/blog/how-to-integrate-google-login-in-your-django-rest-api-using-the-dj-rest-auth-library
    # https://dj-rest-auth.readthedocs.io/en/latest/installation.html

    # Helpfull urls:
    # https://console.cloud.google.com/apis/credentials?organizationId=854549492366&project=expanded-goal-388913
    # https://developers.google.com/oauthplayground/

    # This is for getting code after selecting auth emailaccount.
    # https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fredirect&prompt=consent&response_type=code&client_id=75689505196-425ppqj1ggje4mlt8958s5ga4l7tpgo6.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline&service=lso&o2v=2&flowName=GeneralOAuthFlow
]
