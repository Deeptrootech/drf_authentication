from django.urls import path
from .views import LoginAPIView, RegistrationAPIView, VerifyOTPView, ForgotPasswordView, ResetPasswordView

app_name = 'app_otp_auth'

urlpatterns = [
    path('api/auth/register', RegistrationAPIView.as_view()),  # Registeration
    path('api/auth/login', LoginAPIView.as_view()),  # Login after otp verification
    path('api/auth/verify', VerifyOTPView.as_view()),  # otp Verify
    path('api/auth/forgot', ForgotPasswordView.as_view(), name='forgot-password'),  # forgot Password
    path('api/auth/reset', ResetPasswordView.as_view(), name='reset-password'),  # Resetting the Password after Login

]
