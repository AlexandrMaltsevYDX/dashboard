from .country import CountryModelViewSet
from .region import RegionModelViewSet
from .city import CityModelViewSet
from .district import DistrictModelViewSet
from .tag import TagModelViewSet
from .street import StreetModelViewSet
from .coordinates import CoordinatesModelViewSet
from .place import PlaceModelViewSet

__all__ = [
    "PlaceModelViewSet",
    "CountryModelViewSet",
    "RegionModelViewSet",
    "CityModelViewSet",
    "DistrictModelViewSet",
    "TagModelViewSet",
    "StreetModelViewSet",
    "CoordinatesModelViewSet",
]
