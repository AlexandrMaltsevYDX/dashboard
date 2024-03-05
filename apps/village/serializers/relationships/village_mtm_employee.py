from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.village import models, serializers


class VillageEmployeeModelSerializer(ModelSerializer):
    employee = SlugRelatedField(
        read_only=True,
        slug_field="uuid",
    )

    class Meta:
        model = models.relationships.VillageEmployee
        fields = [
            "employee",
        ]
