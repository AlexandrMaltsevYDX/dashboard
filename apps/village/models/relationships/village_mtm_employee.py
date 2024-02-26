from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from .. import (
    village,
)

from apps.users.models import EmployeeProfileModel


class VillageEmployee(BaseModel):
    village = ForeignKey(
        village.Village,
        on_delete=CASCADE,
        related_name="villageemployees",
    )
    employee = ForeignKey(
        EmployeeProfileModel,
        on_delete=CASCADE,
        related_name="villageagents",
    )

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Агенты"
        verbose_name_plural = "Агенты"
