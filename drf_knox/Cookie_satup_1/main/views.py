from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import LoginSerializer, RegisterSerializer, PasswordChangeSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import serializers
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.core.exceptions import ImproperlyConfigured
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model, logout

from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if not request.data['username'] == "admin":
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)

            return super(LoginView, self).post(request, format=None)
        else:
            raise APIException("Not Allowed login as admin username")


class RegisterUserView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        # seralized and resistered user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)

        # In case if you need to generate token for registered user
        # data = serializers.AuthUserSerializer(user).data
        return Response(status=status.HTTP_201_CREATED)


class ChangepasswordView(generics.CreateAPIView):
    serializer_class = serializers.PasswordChangeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
