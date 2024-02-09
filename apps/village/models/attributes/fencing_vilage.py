from django.db import models
from apps.core.models.base import BaseModel


class FencingVillage(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Ограждение поселка",
        help_text="Введите текстовое значение",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ограждение поселка"
        verbose_name_plural = "Ограждение поселка"
