from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from apps.reobjects import models
from . import (
    reobject,
    image,
)


class ReObjectEngineeringServices(BaseModel):
    re_object = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
        related_name="re_objects",
    )
    engineering_service = ForeignKey(
        models.attributes.EngineeringServices,
        on_delete=CASCADE,
        related_name="engineering_services",
        verbose_name="Коммуникации",
    )

    class Meta:
        verbose_name = "Инженерные коммуникации"
        verbose_name_plural = "Инженерные коммуникации"
