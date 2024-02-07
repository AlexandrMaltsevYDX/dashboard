from apps.applications import serializers, models
from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)


class AnnotationsImageSerializers(ModelSerializer):
    class Meta:
        model = models.application.ApplicationImageModel
        fields = "__all__"
