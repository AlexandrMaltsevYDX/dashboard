from django.db import models
from apps.core.models.base import BaseModel


class WindowMaterial(BaseModel):
    name = models.CharField(
        max_length=50,
        verbose_name="Материал окон",
        help_text="Материал окон",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Материал окон"
        verbose_name_plural = "Материал окон"
