from django.db import models
from apps.core.models.base import BaseModel


class VisibleOnSite(BaseModel):
    value = models.CharField(
        max_length=50,
        verbose_name="Страница отображения",
        help_text="Введите текст",
        blank=True,
    )

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Страница отображения"
        verbose_name_plural = "Страница отображения"
