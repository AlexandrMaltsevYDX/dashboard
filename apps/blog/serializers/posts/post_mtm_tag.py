from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.blog import models, serializers


class PostTagsModelSerializer(ModelSerializer):
    # engineering_service = SlugRelatedField(read_only=True, slug_field="value")

    class Meta:
        model = models.posts.PostTagsModel
        fields = "__all__"
