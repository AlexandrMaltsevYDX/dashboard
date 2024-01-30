from django.db.models import ForeignKey, FileField, CASCADE, CharField

from apps.core.models.base import BaseModel
from .post import Post


class Tag(BaseModel):
    name = CharField(
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Тэг поста"
        verbose_name_plural = "Тэги поста"
