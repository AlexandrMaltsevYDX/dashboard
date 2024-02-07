from django.urls import path, include
from apps.reviews import routers

urlpatterns = [
    path("", include(routers.review.router.urls)),
]
