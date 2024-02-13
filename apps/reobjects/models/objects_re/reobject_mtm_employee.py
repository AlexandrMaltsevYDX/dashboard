from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from . import (
    reobject,
)

from apps.users.models import EmployeeProfileModel


class ReObjectEmployee(BaseModel):
    re_object = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
        related_name="reobjectemployees",
    )
    employee = ForeignKey(
        EmployeeProfileModel,
        on_delete=CASCADE,
        related_name="agents",
    )
