from django.urls import path, include
from apps.village import routers

urlpatterns = [
    path("", include(routers.village.router.urls)),
]
