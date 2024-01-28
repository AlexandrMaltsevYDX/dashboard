from django.db import models
from apps.core.models.base import BaseModel


class ReliefArea(BaseModel):
    value = models.CharField(
        max_length=255,
        verbose_name="Рельеф участка",
        help_text="Рельеф участка",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Рельеф участка"
        verbose_name_plural = "Рельеф участка"
