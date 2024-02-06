from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)
from apps.blog import models, serializers
from .image import PostImageModelSerializer
from .post_mtm_tag import PostTagsModelSerializer


class PostModelSerializer(ModelSerializer):
    photos = PostImageModelSerializer(
        many=True,
        read_only=True,
    )
    images = ListField(child=FileField(required=False), write_only=True)
    tags = PostTagsModelSerializer(
        many=True,
        read_only=True,
        source="posts",
    )

    class Meta:
        model = models.posts.Post
        fields = "__all__"