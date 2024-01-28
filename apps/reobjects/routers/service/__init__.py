from rest_framework.routers import DefaultRouter
from apps.reobjects import viewsets

router = DefaultRouter()


router.register(
    prefix=r"",
    viewset=viewsets.service.ServiceModelViewSet,
)
