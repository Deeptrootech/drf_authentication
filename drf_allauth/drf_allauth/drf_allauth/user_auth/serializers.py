from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    """
    Problem2: register user url is getting inherited here
    """
    phone_number = serializers.CharField(max_length=30)
    # Define transaction.atomic to rollback the save operation in case of error

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('gender')
        user.phone_number = self.data.get('phone_number')
        user.save()
        return user


