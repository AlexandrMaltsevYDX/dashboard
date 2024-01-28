from django.db import models
from apps.core.models.base import BaseModel


class EngineeringServices(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Инженерные сети",
        help_text="Наличие инженерных сетей",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Инженерные сети"
        verbose_name_plural = "Инженерные сети"
