from django.db.models import ForeignKey, FileField, CASCADE

from apps.core.models.base import BaseImageModel
from .post import Post


class PostImageModel(BaseImageModel):
    objectModel = ForeignKey(
        Post,
        related_name="postimages",
        on_delete=CASCADE,
    )
    image = FileField(upload_to="avatars/")

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = "Фото поста"
        verbose_name_plural = "Фото поста"
