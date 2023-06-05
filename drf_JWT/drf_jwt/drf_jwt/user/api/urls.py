from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, CreateUserAPIView

app_name = "user_api"

router = SimpleRouter()

router.register("users", UserViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("user_create", CreateUserAPIView.as_view(), name="user-create")
]


urlpatterns += router.urls

