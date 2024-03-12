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


class VillagePlanModel(BaseImageModel):
    objectModel = ForeignKey(
        Village,
        related_name="villageplans",
        on_delete=CASCADE,
    )

    image = FileField(upload_to="village/plans/")

    order = PositiveIntegerField(
        verbose_name="Порядок",
        help_text="введите число",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "План поселка"
        verbose_name_plural = "Планы поселков"
