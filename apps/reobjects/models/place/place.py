from django.db import models

from apps.core.models.base import BaseModel
from . import (
    Country,
    Region,
    City,
    District,
    Street,
    Tag,
    Coordinates,
)


class Place(BaseModel):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Страна",
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Регион",
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Город",
    )

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Район",
    )

    street = models.ForeignKey(
        Street,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Улица",
    )

    house = models.PositiveIntegerField(
        null=True,
        verbose_name="Дом",
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Тег",
    )

    flat = models.PositiveIntegerField(
        null=True,
        verbose_name="Квартира",
    )

    coordinates = models.ForeignKey(
        Coordinates,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Координаты",
    )

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house}, {self.tag}, {self.flat}"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
