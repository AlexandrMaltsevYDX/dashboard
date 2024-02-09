from django.contrib import admin
from . import models
from ..reobjects.models.attributes import EngineeringServices

admin.site.register(models.attributes.AreaOfPlotMeasurement)
admin.site.register(models.attributes.CategoryLandPlot)
admin.site.register(models.attributes.ReliefAreaPlot)
admin.site.register(models.attributes.FencingVillage)
admin.site.register(models.attributes.SecurityVillage)


class EngineeringVillageServices(EngineeringServices):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Инженерные сети"
        verbose_name_plural = "Инженерные сети"


admin.site.register(EngineeringVillageServices)
