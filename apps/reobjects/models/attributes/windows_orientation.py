from django.db import models
from apps.core.models.base import BaseModel


class WindowsOrientation(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Ориентация окон",
        help_text="Ориентация окон",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Ориентация окон"
        verbose_name_plural = "Ориентация окон"
