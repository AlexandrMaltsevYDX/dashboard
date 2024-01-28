from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from . import (
    reobject,
)
from apps.reobjects import models


class ReObjectEngineeringServices(BaseModel):
    re_object = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
    )
    engineering_service = ForeignKey(
        models.attributes.EngineeringServices,
        on_delete=CASCADE,
    )
