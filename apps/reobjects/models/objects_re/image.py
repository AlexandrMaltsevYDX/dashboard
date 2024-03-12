from django.db.models import (
    ForeignKey,
    CASCADE,
    FileField,
    PositiveIntegerField,
)

# models
from apps.core.models.base import BaseModel
from . import (
    reobject,
)


class ReObjectImage(BaseModel):
    objectModel = ForeignKey(
        reobject.ReObject,
        related_name="photo_images",
        on_delete=CASCADE,
    )
    image = FileField(upload_to="reobjects/")

    order = PositiveIntegerField(
        verbose_name="Порядок",
        help_text="введите число",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = "Фото объекта"
        verbose_name_plural = "Фото объекта"
