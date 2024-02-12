from django.db import models
from apps.core.models.base import BaseModel


class SalesMethod(BaseModel):
    name = models.CharField(
        max_length=50,
        verbose_name="Способ продажи",
        help_text="Способ продажи(нужно пояснение расширить)",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ продажи"
        verbose_name_plural = "Способ продажи"
