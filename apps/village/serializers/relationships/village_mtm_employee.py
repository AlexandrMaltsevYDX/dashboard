from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.village import models, serializers


class VillageEmployeeModelSerializer(ModelSerializer):
    employee = StringRelatedField(
        read_only=True,
    )

    class Meta:
        model = models.relationships.VillageEmployee
        fields = [
            "employee",
        ]
