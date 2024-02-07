from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)
from .image import AnnotationsImageSerializers
from apps.applications import models


class AnnotationModelSerializer(ModelSerializer):
    photos = AnnotationsImageSerializers(
        source="applicationimages",
        many=True,
        read_only=True,
    )
    images = ListField(
        child=FileField(required=False),
        write_only=True,
        required=False,
    )

    class Meta:
        model = models.application.Application
        fields = [
            "text",
            "applicant",
            "contact",
            "images",
            "photos",
        ]

    def save(self, *args, **kwargs):
        # print("===========>     validated_data", self.validated_data)
        images_data = self.validated_data.pop("images")
        super().save(*args, **kwargs)
        if images_data:
            self.instance.applicationimages.all().delete()
            for image in images_data:
                self.instance.applicationimages.create(image=image)
        return self.instance
