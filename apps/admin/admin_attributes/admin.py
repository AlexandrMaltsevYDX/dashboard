from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TypeHouse)
class TypeHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WindowsOrientation)
class WindowsOrientationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LandCategory)
class LandCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReliefArea)
class ReliefAreaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Fencing)
class FencingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Foundation)
class FoundationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WallMaterial)
class WallMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EngineeringServices)
class EngineeringServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VillageFences)
class VillageFencesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ObjectDescription)
class ObjectDescriptionAdmin(admin.ModelAdmin):
    pass
