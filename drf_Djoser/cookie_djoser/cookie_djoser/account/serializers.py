from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserCreateSerializer):
    """
    Problem: not able to inherit fields (to add extra field while registration)

    This is inherited because if you want to customize user registration validation and all
    """
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ("id", "name", "email", "username", "first_name", "last_name", "password")
