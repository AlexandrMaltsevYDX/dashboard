from rest_framework.routers import DefaultRouter
from apps.village import viewsets

router = DefaultRouter()

router.register(
    prefix=r"villages",
    viewset=viewsets.village.VillageModelViewSet,
)

router.register(
    prefix=r"villages_images",
    viewset=viewsets.village.VillageImageModelViewSet,
)

router.register(
    prefix=r"villages_plans",
    viewset=viewsets.village.VillagePlanModelViewSet,
)

router.register(
    prefix=r"object_invillages",
    viewset=viewsets.relationships.ReObjectInVillagesModelViewSet,
)
