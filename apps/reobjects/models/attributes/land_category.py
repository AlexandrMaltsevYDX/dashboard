from django.db import models
from apps.core.models.base import BaseModel


class LandCategory(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Категория земли",
        help_text="Категория земли",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Категория земель"
        verbose_name_plural = "Категория земель"
