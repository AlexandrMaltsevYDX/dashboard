from django.urls import path, include
from apps.applications import routers

urlpatterns = [
    path("", include(routers.application.router.urls)),
]
