from django.db import models

from apps.core.models.base import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Страна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
