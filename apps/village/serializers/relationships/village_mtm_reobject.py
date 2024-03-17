from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from rest_framework.relations import SlugRelatedField

from apps.village import models


class ReObjectInVillagesModelSerializer(ModelSerializer):
    village = SlugRelatedField(
        read_only=True,
        slug_field="uuid",
    )
    re_object_in_villages = SlugRelatedField(
        read_only=True,
        slug_field="uuid",
    )

    class Meta:
        model = models.relationships.ReObjectInVillages
        fields = [
            "village",
            "re_object_in_villages",
        ]
