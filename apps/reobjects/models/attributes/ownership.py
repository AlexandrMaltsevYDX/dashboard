from django.db import models
from apps.core.models.base import BaseModel


class Ownership(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Форма собственности",
        help_text="Форма собственности объекта",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Тип собственности"
        verbose_name_plural = "Тип собственности"
