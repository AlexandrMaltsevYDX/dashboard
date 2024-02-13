from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.reobjects import models, serializers


class ReObjectEmployeeModelSerializer(ModelSerializer):
    employee = StringRelatedField(
        read_only=True,
    )

    class Meta:
        model = models.objects_re.ReObjectEmployee
        fields = [
            "employee",
        ]
