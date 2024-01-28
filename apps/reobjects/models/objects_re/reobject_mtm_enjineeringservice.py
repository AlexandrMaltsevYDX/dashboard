from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from . import (
    reobject,
    images,
)


class ReObjectMedia(BaseModel):
    re_object = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
    )
    media = ForeignKey(
        images.ReImage,
        on_delete=CASCADE,
    )
