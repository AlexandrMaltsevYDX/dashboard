from django.db import models
from apps.core.models.base import BaseModel


class Coordinates(BaseModel):
    yandex_latitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Широта (Yandex)",
    )

    yandex_longitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Долгота (Yandex)",
    )

    def __str__(self):
        return f"{self.yandex_latitude}, {self.yandex_longitude}"

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"
