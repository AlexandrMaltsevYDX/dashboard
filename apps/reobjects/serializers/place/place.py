from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    StringRelatedField,
)
from apps.reobjects import models
from . import city
from . import coordinates
from . import country
from . import district
from . import region
from . import street
from . import tag


class PlaceModelSerializer(ModelSerializer):
    # city = city.CityModelSerializer(read_only=True)
    # coordinates = coordinates.CoordinatesModelSerializer(read_only=True)
    # country = country.CountryModelSerializer(read_only=True)
    # district = district.DistrictModelSerializer(read_only=True)
    # region = region.RegionModelSerializer(read_only=True)
    # street = street.StreetModelSerializer(read_only=True)
    # tag = tag.TagModelSerializer(read_only=True)
    city = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    coordinates = StringRelatedField(
        read_only=True,
    )
    country = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    district = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    region = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    street = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    tag = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = models.place.Place
        fields = "__all__"
