from apps.reviews import models, serializers
from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)


class ReviewImageSerializers(ModelSerializer):
    class Meta:
        model = models.review.ReviewImageModel
        fields = "__all__"
