from rest_framework.routers import DefaultRouter
from apps.reobjects import viewsets


router = DefaultRouter()

router.register(
    prefix=r"category",
    viewset=viewsets.attributes.CategoryModelViewSet,
)
router.register(
    prefix=r"engineering-services",
    viewset=viewsets.attributes.EngineeringServicesModelViewSet,
)
router.register(
    prefix=r"fencing",
    viewset=viewsets.attributes.FencingModelViewSet,
)
router.register(
    prefix=r"foundation",
    viewset=viewsets.attributes.FoundationModelViewSet,
)
router.register(
    prefix=r"land-category",
    viewset=viewsets.attributes.LandCategoryModelViewSet,
)
router.register(
    prefix=r"ownership",
    viewset=viewsets.attributes.OwnershipModelViewSet,
)
router.register(
    prefix=r"relief",
    viewset=viewsets.attributes.ReliefAreaModelViewSet,
)
router.register(
    prefix=r"type-house",
    viewset=viewsets.attributes.TypeHouseModelViewSet,
)
router.register(
    prefix=r"village-fences",
    viewset=viewsets.attributes.VillageFencesModelViewSet,
)
router.register(
    prefix=r"windows-orientation",
    viewset=viewsets.attributes.WindowsOrientationModelViewSet,
)
router.register(
    prefix=r"wall-material",
    viewset=viewsets.attributes.WallMaterialModelViewSet,
)
router.register(
    prefix=r"object-description",
    viewset=viewsets.attributes.ObjectDescriptionModelViewSet,
)

router.register(
    prefix=r"coordinates",
    viewset=viewsets.attributes.CoordinatesModelViewSet,
)