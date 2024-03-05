from django.db.models import (
    ForeignKey,
    CASCADE,
    FileField,
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

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Фото поселка"
        verbose_name_plural = "Фото поселков"
