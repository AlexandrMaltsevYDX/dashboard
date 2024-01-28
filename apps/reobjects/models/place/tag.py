from django.db import models

from apps.core.models.base import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Тег")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
