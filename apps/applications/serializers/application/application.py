from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)
from .image import AnnotationsImageSerializers
from apps.applications import models


class AnnotationModelSerializer(ModelSerializer):
    class Meta:
        model = models.application.Application
        fields = [
            "text",
            "applicant",
            "contact",
        ]
