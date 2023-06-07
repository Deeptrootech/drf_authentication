from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

MyUser = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user


class VerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['otp', 'email']


class ForgotPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = MyUser
        fields = ('email',)


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    old_password = serializers.CharField(max_length=255)
    new_password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    class Meta:
        model = MyUser
        fields = ('email', 'old_password', 'new_password', 'confirm_password')


class LoginSerializer(TokenObtainPairSerializer):
    """
    LoginSerializer: which will authenticate credentials into database and generate jwt token.

    Here, we preferred email to username.
    because we have (USERNAME_FIELD = 'email') in UserMaster Model.
    """
    email = serializers.CharField(max_length=255)
    # username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        fields = ('email', 'password', 'token')

    def validate(self, data):
        breakpoint()
        # If we want to add custom validation before calling superuser's validate method
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # Below will call TokenObtainPairSerializers' validate() method
        token_data = super().validate(data)
        # this token_data will be from TokenObtainPairSerializers' validate() method
        # and will have tokens (access and refresh).
        # to see click: TokenObtainPairSerializer

        # here, adding tokens in data dict and return them as validated_data.
        data.update({"token": token_data, "user": self.user})
        return data
