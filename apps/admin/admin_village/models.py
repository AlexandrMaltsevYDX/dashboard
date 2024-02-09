from django.db import models
from apps.village.models.village import Village


# Create your models here.
class VillageProxy(Village):
    def __str__(self):
        return f"{self.uuid}"

    class Meta:
        proxy = True
        verbose_name = "Поселок"
        verbose_name_plural = "Поселки"
