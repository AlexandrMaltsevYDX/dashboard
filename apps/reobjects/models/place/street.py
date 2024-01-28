from django.db import models

from apps.core.models.base import BaseModel


class Street(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Улица")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
