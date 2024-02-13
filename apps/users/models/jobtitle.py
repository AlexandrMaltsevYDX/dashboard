from django.db.models import CharField
from apps.core.models.base import BaseModel


class JobTitle(BaseModel):
    name = CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Название должности",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название должности"
        verbose_name_plural = "Название должности"
