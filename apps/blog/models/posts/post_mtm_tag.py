from django.db.models import ForeignKey, FileField, CASCADE

from apps.core.models.base import BaseImageModel, BaseModel
from .post import Post
from .tag import Tag


class PostTagsModel(BaseModel):
    post = ForeignKey(
        Post,
        related_name="posts_posts",
        on_delete=CASCADE,
    )
    tag = ForeignKey(
        Tag,
        related_name="post_tags",
        on_delete=CASCADE,
    )

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Связанные Тэги"
        verbose_name_plural = "Связанные Тэги"
