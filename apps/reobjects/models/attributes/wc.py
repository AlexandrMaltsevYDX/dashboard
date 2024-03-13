from django.db import models
from apps.core.models.base import BaseModel


class WC(BaseModel):
    value = models.CharField(
        max_length=255,
        verbose_name="Санузел",
        help_text="Санузел",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Санузел"
        verbose_name_plural = "Санузел"
