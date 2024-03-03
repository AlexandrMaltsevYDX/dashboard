from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)
from apps.blog import models, serializers
from .image import PostImageModelSerializer
from .post_mtm_tag import PostTagsModelSerializer
from .tag import TagModelSerializer


class PostModelSerializer(ModelSerializer):
    photos = PostImageModelSerializer(
        many=True,
        read_only=True,
        source="postimages",
    )
    # images = ListField(child=FileField(required=False), write_only=True)
    tags = PostTagsModelSerializer(
        many=True,
        read_only=True,
        source="posts_posts",
        # default=1,
    )
    author = SlugRelatedField(
        slug_field="uuid",
        read_only=True,
    )

    class Meta:
        ordering = ["author"]
        model = models.posts.Post
        fields = [
            "uuid",
            "tags",
            "author",
            "photos",
            "name",
            "body",
        ]
