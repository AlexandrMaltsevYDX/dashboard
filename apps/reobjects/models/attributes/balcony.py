from django.db import models
from apps.core.models.base import BaseModel


class Balcony(BaseModel):
    name = models.CharField(
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип балкона/лоджии"
        verbose_name_plural = "Тип балкона/лоджии"
