from django.urls import path, include
from apps.users.routers import router as user_router
from apps.users.routers import profile_images_router


# from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("user/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", include(user_router.urls)),
    path("", include(profile_images_router.urls)),
]
