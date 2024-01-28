from django.db import models
from apps.core.models.base import BaseModel


class WallMaterial(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Материал стен",
        help_text="Материал стен",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Материал стен"
        verbose_name_plural = "Материал стен"
