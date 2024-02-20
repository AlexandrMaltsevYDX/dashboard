from django.db import models
from apps.core.models.base import BaseModel


class Lift(BaseModel):
    value = models.CharField(
        max_length=300,
        verbose_name="Лифт",
        help_text="Лифт",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Лифт"
        verbose_name_plural = "Лифт"
