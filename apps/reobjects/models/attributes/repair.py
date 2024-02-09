from django.db import models
from apps.core.models.base import BaseModel


class Repair(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Ремонт",
        help_text="Введите тектс",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонт"
