from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from . import (
    reobject,
)


class ReObjectClose(BaseModel):
    re_object = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
        related_name="reobjectbase",
    )
    close_re_object = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
        related_name="reobjectclose",
        verbose_name="Похожий объект",
    )

    class Meta:
        verbose_name = "Похожие объекты"
        verbose_name_plural = "Похожие объекты"
