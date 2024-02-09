from django.db import models
from apps.core.models.base import BaseModel


class SecurityVillage(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Охрана поселка",
        help_text="Введите текстовое значение",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Охрана поселка"
        verbose_name_plural = "Охрана поселка"
