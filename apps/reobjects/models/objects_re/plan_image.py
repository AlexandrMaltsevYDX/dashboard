from django.db.models import (
    ForeignKey,
    CASCADE,
    RESTRICT,
    FileField,
)

from apps.core.models.base import (
    BaseModel,
    BaseImageModel,
)

from .reobject import ReObject


class ReObjectPlanModel(BaseImageModel):
    re_object = ForeignKey(
        ReObject,
        related_name="reobjectplans",
        on_delete=CASCADE,
    )

    image = FileField(upload_to="reobjects/plans/")

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Планировка объекта"
        verbose_name_plural = "Планировки объектов"
