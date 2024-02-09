from django.db import models
from apps.core.models.base import BaseModel


class EngineeringServices(BaseModel):
    name = models.CharField(
        max_length=50,
        verbose_name="Инженерные сети",
        help_text="Наличие инженерных сетей",
        blank=True,
    )

    tag = models.CharField(
        max_length=50,
        verbose_name="tag",
        help_text="внесите метку для более удобного визуального поиска, например id поселка, или '4.4 кВт - 15 кВт'",
        blank=True,
        null=True,
    )

    short_text = models.TextField(
        verbose_name="Короткое описание",
        help_text="Hапример: '4.4 кВт - 15 кВт' ",
        blank=True,
        null=True,
    )

    text = models.TextField(
        verbose_name="Полное описание описание",
        help_text="Hапример: 'На дом площадью менее 150 м2 от 4.4 кВт (включено в стоимость дома) и на дома более 150 м2 от 5,5 кВт (включено в стоимость дома) с возможностью увеличения до 15 кВт (35 000 руб. за кВт)' ",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}: {self.tag}:"

    class Meta:
        verbose_name = "Инженерные сети"
        verbose_name_plural = "Инженерные сети"
