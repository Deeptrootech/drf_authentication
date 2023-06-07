from django.urls import path
from .views import LoginAPIView, RegistrationAPIView, VerifyOTPView, ForgotPasswordView, ResetPasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'app_otp_auth'

urlpatterns = [
    # JWT Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # App Authentication
    path('api/auth/register', RegistrationAPIView.as_view()),  # Registeration
    path('api/auth/login', LoginAPIView.as_view()),  # Login after otp verification
    path('api/auth/verify', VerifyOTPView.as_view()),  # otp Verify
    path('api/auth/forgot', ForgotPasswordView.as_view(), name='forgot-password'),  # forgot Password
    path('api/auth/reset', ResetPasswordView.as_view(), name='reset-password'),  # Resetting the Password after Login

]
