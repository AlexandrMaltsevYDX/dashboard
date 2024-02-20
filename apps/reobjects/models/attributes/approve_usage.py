from django.db import models
from apps.core.models.base import BaseModel


class ApproveUsage(BaseModel):
    value = models.TextField(
        verbose_name="Разрешенное использование",
        help_text="Разрешенное использование",
        blank=True,
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Разрешенное использование"
        verbose_name_plural = "Разрешенное использование"
