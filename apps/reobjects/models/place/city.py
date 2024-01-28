from django.db import models
from apps.core.models.base import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Город")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
