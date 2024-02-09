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


class VillagePlanModel(BaseImageModel):
    village = ForeignKey(
        Village,
        related_name="villageplans",
        on_delete=CASCADE,
    )

    image = FileField(upload_to="village/plans/")

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "План поселка"
        verbose_name_plural = "Планы поселков"