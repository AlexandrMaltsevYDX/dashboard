from django.db import models

from apps.core.models.base import BaseModel
from mdeditor.fields import MDTextField


class Service(BaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    main_text = models.CharField(
        max_length=255,
        verbose_name="Текст для заголовка на странице Услуги",
        blank=True,
    )

    secondary_text = MDTextField(
        null=True,
        blank=True,
        verbose_name="Текст описание в блоке УСЛУГИ",
        help_text="Текст с форматированием",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
