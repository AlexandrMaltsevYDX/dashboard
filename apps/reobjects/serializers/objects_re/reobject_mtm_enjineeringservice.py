from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.reobjects import models, serializers


class ReObjectEngineeringServicesModelSerializer(ModelSerializer):
    engineering_service = SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = models.objects_re.ReObjectEngineeringServices
        fields = [
            "engineering_service",
        ]
