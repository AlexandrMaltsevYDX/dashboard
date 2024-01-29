from rest_framework.routers import DefaultRouter
from apps.reobjects import viewsets


router = DefaultRouter()

router.register(
    prefix=r"objects",
    viewset=viewsets.objects_re.ReObjectModelViewSet,
)
