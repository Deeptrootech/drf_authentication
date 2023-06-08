from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer

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


class LoginSerializer(TokenObtainSerializer):
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

        # 1) Only to authenticate user from database (`coz using 2F varification)
        authenticated_user = super().validate(data)
        breakpoint()
        if self.user is not None and self.user.is_confirmed and self.user.is_active:
            refresh = self.get_token(self.user)

            refresh = str(refresh)
            access = str(refresh.access_token)

            token_data = {"refresh": refresh, "access": access}
            if api_settings.UPDATE_LAST_LOGIN:
                update_last_login(None, self.user)

            data.update({"token": token_data, "user": self.user})
            return data
        raise serializers.ValidationError('Account may not approved or wrong Password.')

        # # 2) To authenticate user and Get access and refresh tokens. (`coz not using 2F varification)
        # # Below will call TokenObtainPairSerializers' validate() method
        # token_data = super().validate(data)
        # # this token_data will be from TokenObtainPairSerializer's validate() method
        # # and will have tokens (access and refresh).
        # # to see click: TokenObtainPairSerializer
        #
        # # here, adding tokens in data dict and return them as validated_data.
        # data.update({"token": token_data, "user": self.user})
        # return data
