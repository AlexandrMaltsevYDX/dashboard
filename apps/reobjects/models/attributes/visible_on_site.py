from django.db import models
from apps.core.models.base import BaseModel


class VisibleOnSite(BaseModel):
    value = models.CharField(
        max_length=255,
        verbose_name="Страница отображения",
        help_text="Введите текст",
        blank=True,
        null=True,
    )

    type_value = models.CharField(
        max_length=255,
        verbose_name="Псевдоним названия страниц",
        help_text="Введите текст латиницей в формате 'word-word-word'",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Страница отображения"
        verbose_name_plural = "Страница отображения"
