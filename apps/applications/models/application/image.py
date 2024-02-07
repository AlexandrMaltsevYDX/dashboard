from django.db import models

from apps.core.models.base import BaseModel, BaseImageModel
from .application import Application


class ApplicationImageModel(BaseImageModel):
    application = models.ForeignKey(
        Application,
        related_name="applicationimages",
        on_delete=models.CASCADE,
    )
    image = models.FileField(upload_to="applications/")

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Фото к заявке"
        verbose_name_plural = "Фото к заявке"
