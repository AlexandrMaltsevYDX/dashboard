from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.blog import models, serializers
from .tag import TagModelSerializer


class PostTagsModelSerializer(ModelSerializer):
    tag = TagModelSerializer()

    class Meta:
        ordering = ["tag"]
        model = models.posts.PostTagsModel
        fields = "__all__"
