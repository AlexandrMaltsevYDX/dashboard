from rest_framework.routers import DefaultRouter
from apps.reviews import viewsets

router = DefaultRouter()

router.register(
    prefix=r"reviews",
    viewset=viewsets.review.ReviewModelViewSet,
)
