from django.db import models
from apps.core.models.base import BaseModel


class Driveways(BaseModel):
    name = models.CharField(
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подъездные пути"
        verbose_name_plural = "Подъездные пути"
