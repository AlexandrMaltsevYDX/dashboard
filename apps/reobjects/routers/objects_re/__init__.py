from rest_framework.routers import DefaultRouter
from apps.reobjects import viewsets


router = DefaultRouter()

router.register(
    prefix=r"objects",
    viewset=viewsets.objects_re.ReObjectModelViewSet,
)

router.register(
    prefix=r"objects_islike",
    viewset=viewsets.objects_re.ReObjectCloseModelViewSet,
)

router.register(
    prefix=r"objects_images",
    viewset=viewsets.objects_re.ReObjectImageModelViewSet,
)

router.register(
    prefix=r"objects_plans",
    viewset=viewsets.objects_re.ReObjectPlanModelViewSet,
)
