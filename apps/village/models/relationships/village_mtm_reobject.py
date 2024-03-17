from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from apps.reobjects.models.objects_re import reobject
from .. import (
    village,
)


class ReObjectInVillages(BaseModel):
    village = ForeignKey(
        village.Village,
        on_delete=CASCADE,
        related_name="villagebase",
    )
    re_object_in_villages = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
        related_name="reobjectinvilages",
        verbose_name="Объект",
    )

    class Meta:
        verbose_name = "Объекты в поселке"
        verbose_name_plural = "Объекты в поселке"
