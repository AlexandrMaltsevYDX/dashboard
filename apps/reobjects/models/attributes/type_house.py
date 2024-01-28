from django.db import models
from apps.core.models.base import BaseModel


class TypeHouse(BaseModel):
    name = models.CharField(
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип объекта"
        verbose_name_plural = "Тип объекта"
