from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = "main"

urlpatterns = [
    # jwt_views
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # generate token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # verify token
]
