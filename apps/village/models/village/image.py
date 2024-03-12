from django.db.models import (
    ForeignKey,
    CASCADE,
    FileField,
    PositiveIntegerField,
)

from apps.core.models.base import (
    BaseModel,
    BaseImageModel,
)

from .village import Village


class VillageImageModel(BaseImageModel):
    objectModel = ForeignKey(
        Village,
        related_name="villageimages",
        on_delete=CASCADE,
    )

    image = FileField(upload_to="village/images/")

    order = PositiveIntegerField(
        verbose_name="Порядок",
        help_text="введите число",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Фото поселка"
        verbose_name_plural = "Фото поселков"
