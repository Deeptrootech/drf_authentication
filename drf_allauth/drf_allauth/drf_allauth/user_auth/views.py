from django.shortcuts import render
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from settings.base import LOGIN_REDIRECT_URL


# Create your views here.


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLoginView(SocialLoginView):
    """ if you want to use Authorization Code Grant, use this """
    adapter_class = GoogleOAuth2Adapter
    callback_url = LOGIN_REDIRECT_URL
    client_class = OAuth2Client