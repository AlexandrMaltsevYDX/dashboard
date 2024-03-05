from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.reobjects import models, serializers


class ReObjectEmployeeModelSerializer(ModelSerializer):
    employee = SlugRelatedField(
        read_only=True,
        slug_field="uuid",
    )

    class Meta:
        model = models.objects_re.ReObjectEmployee
        fields = [
            "employee",
        ]
