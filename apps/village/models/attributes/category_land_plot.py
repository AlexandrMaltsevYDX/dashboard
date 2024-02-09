from django.db.models import CharField
from apps.core.models.base import BaseModel


class CategoryLandPlot(BaseModel):
    name = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Категория земель",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория земель"
        verbose_name_plural = "Категория земель"
