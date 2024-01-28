from django.db import models
from apps.core.models.base import BaseModel


class ObjectDescription(BaseModel):
    value = models.TextField(
        max_length=2500,
        verbose_name="Описание объекта",
        help_text="Используйте маркдаун",
        blank=True,
    )

    def __str__(self):
        return self.value[:25]

    class Meta:
        verbose_name = "Описание объекта"
        verbose_name_plural = "Описание объекта"
