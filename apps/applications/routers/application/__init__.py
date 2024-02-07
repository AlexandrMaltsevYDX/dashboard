from rest_framework.routers import DefaultRouter
from apps.applications import viewsets

router = DefaultRouter()

router.register(
    prefix=r"applications",
    viewset=viewsets.application.ApplicationModelViewSet,
)
