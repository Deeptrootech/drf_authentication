import os, jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, PermissionsMixin, AbstractUser)
from django.db import models
import uuid
from uuid import UUID


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.

    Ref. https://testdriven.io/blog/django-custom-user-model/
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class UserMaster(AbstractUser):
    user_id = models.CharField(primary_key=True, default=uuid.uuid4, blank=False, unique=True, editable=False,
                               max_length=500, name=("user_id"), verbose_name=("User ID"))
    username = None
    mobile = models.CharField(max_length=11, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_confirmed = models.BooleanField(default=False)  # default is True when not using otp email verification
    otp = models.IntegerField(editable=False, default=False)  # storing otp
    is_used = models.BooleanField(default=False)  # it becomes true when otp stored in db is already used

    USERNAME_FIELD = 'email'  # by default it takes username. but we  change  to  email
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return "{}".format(self.user_id)
