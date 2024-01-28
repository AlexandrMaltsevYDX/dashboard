from django.db import models

from apps.core.models.base import BaseModel


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
    secondary_text = models.CharField(
        max_length=255,
        verbose_name="Текст описание в блоке УСЛУГИ",
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
