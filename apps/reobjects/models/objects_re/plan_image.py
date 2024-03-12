from django.db.models import (
    ForeignKey,
    CASCADE,
    RESTRICT,
    FileField,
    PositiveIntegerField,
)

from apps.core.models.base import (
    BaseModel,
    BaseImageModel,
)

from .reobject import ReObject


class ReObjectPlanModel(BaseImageModel):
    objectModel = ForeignKey(
        ReObject,
        related_name="plans_images",
        on_delete=CASCADE,
    )

    image = FileField(upload_to="reobjects/plans/")

    order = PositiveIntegerField(
        verbose_name="Порядок",
        help_text="введите число",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "План объекта"
        verbose_name_plural = "Планы объекта"
