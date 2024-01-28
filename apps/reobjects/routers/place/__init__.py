from rest_framework.routers import DefaultRouter
from apps.reobjects import viewsets

router = DefaultRouter()


router.register(
    prefix=r"city",
    viewset=viewsets.place.CityModelViewSet,
)

router.register(
    prefix=r"coordinates",
    viewset=viewsets.place.CoordinatesModelViewSet,
)


router.register(
    prefix=r"country",
    viewset=viewsets.place.CountryModelViewSet,
)

router.register(
    prefix=r"district",
    viewset=viewsets.place.DistrictModelViewSet,
)


router.register(
    prefix=r"place",
    viewset=viewsets.place.PlaceModelViewSet,
)

router.register(
    prefix=r"region",
    viewset=viewsets.place.RegionModelViewSet,
)


router.register(
    prefix=r"street",
    viewset=viewsets.place.StreetModelViewSet,
)


router.register(
    prefix=r"tag",
    viewset=viewsets.place.TagModelViewSet,
)
