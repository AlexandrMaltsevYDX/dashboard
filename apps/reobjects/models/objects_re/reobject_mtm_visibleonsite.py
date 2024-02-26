from django.db.models import ForeignKey, CASCADE

# models
from apps.core.models.base import BaseModel
from apps.reobjects import models
from . import (
    reobject,
    image,
)


class ReObjectVisibleOnSite(BaseModel):
    re_object = ForeignKey(
        reobject.ReObject,
        on_delete=CASCADE,
        related_name="reobjectsite",
    )

    display_pages = ForeignKey(
        models.attributes.VisibleOnSite,
        on_delete=CASCADE,
        related_name="pages",
        verbose_name="Страница сайта",
    )

    class Meta:
        verbose_name = "Отображение на сайте"
        verbose_name_plural = "Отображение на сайте"
