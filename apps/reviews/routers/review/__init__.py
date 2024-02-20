from rest_framework.routers import DefaultRouter
from apps.reviews import viewsets

router = DefaultRouter()

router.register(
    prefix=r"reviews",
    viewset=viewsets.review.ReviewModelViewSet,
)


router.register(
    prefix=r"reviews_images",
    viewset=viewsets.review.ReviewImageModelViewSet,
)
