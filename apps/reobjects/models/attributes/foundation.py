from django.db import models
from apps.core.models.base import BaseModel


class Foundation(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Тип фундамента",
        help_text="Тип фундамента",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Тип фундамента"
        verbose_name_plural = "Тип фундамента"
