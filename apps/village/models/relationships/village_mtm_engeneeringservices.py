from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from apps.reobjects import models as reobjects_models
from apps.village import models


class VillageEngineeringServices(BaseModel):
    re_object = ForeignKey(
        models.village.Village,
        on_delete=CASCADE,
        related_name="villages",
    )
    engineering_service = ForeignKey(
        reobjects_models.attributes.EngineeringServices,
        on_delete=CASCADE,
        related_name="village_engineering_services",
    )
