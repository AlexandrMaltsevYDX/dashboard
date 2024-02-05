from django.db.models import (
    ForeignKey,
    CASCADE,
    FileField,
    FloatField,
)
from apps.core.models.base import BaseModel
from .reobject import ReObject


class Coordinates(BaseModel):
    re_object = ForeignKey(
        ReObject,
        related_name="coordinates",
        on_delete=CASCADE,
    )
    ydx_latitude = FloatField(blank=True, null=True, verbose_name="Широта(Яндекс)")
    ydx_longitude = FloatField(blank=True, null=True, verbose_name="Долгота(Яндекс)")

    def __str__(self):
        return f"{self.ydx_latitude}  ,  {self.ydx_longitude}"

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"
