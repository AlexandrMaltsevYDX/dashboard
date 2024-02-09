from django.db.models import CharField
from apps.core.models.base import BaseModel


class AreaOfMeasurement(BaseModel):
    name = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Название единицы измерения",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Единица измерения площади"
        verbose_name_plural = "Единицы измерения площади"
