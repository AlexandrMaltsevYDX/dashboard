from django.db import models
from apps.core.models.base import BaseModel


class Fencing(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Ограждение участка",
        help_text="Ограждение участка",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Ограждение участка"
        verbose_name_plural = "Ограждение участка"
