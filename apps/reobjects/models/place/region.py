from django.db import models

from apps.core.models.base import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Регион")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
