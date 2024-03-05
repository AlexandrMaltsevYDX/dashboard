from django.db import models

from apps.core.models.base import BaseModel, BaseImageModel
from .review import Review


class ReviewImageModel(BaseImageModel):
    objectModel = models.ForeignKey(
        Review,
        related_name="reviewimages",
        on_delete=models.CASCADE,
    )
    image = models.FileField(
        upload_to="reviews/",
    )

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Фото к ревью"
        verbose_name_plural = "Фото к ревью"
