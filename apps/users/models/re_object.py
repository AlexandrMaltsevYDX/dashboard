from django.db import models

from apps.core.models.base import BaseModel


class ReObjectModel(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Объект недвижимости"
        verbose_name_plural = "Объекты недвижимости"
