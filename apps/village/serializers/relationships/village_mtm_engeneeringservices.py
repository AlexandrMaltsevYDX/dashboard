from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from rest_framework.relations import SlugRelatedField

from apps.village import models


class VillageEngineeringServicesModelSerializer(ModelSerializer):
    engineering_service = SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = models.relationships.VillageEngineeringServices
        fields = [
            "engineering_service",
        ]
