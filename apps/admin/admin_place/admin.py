from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Street)
class StreetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    pass
