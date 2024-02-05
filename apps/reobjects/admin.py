from django.contrib import admin
from django.utils.html import format_html
from . import models


admin.site.register(models.attributes.Category)
admin.site.register(models.attributes.TypeHouse)
admin.site.register(models.attributes.WallMaterial)
admin.site.register(models.attributes.WindowsOrientation)
admin.site.register(models.attributes.Ownership)
admin.site.register(models.attributes.LandCategory)
admin.site.register(models.attributes.ReliefArea)
admin.site.register(models.attributes.Fencing)
admin.site.register(models.attributes.Foundation)
admin.site.register(models.attributes.VillageFences)
admin.site.register(models.attributes.EngineeringServices)


class ReObjectImageInline(admin.TabularInline):
    model = models.objects_re.ReObjectImage
    extra = 1


@admin.register(models.objects_re.ReObject)
class ReObjectModel(admin.ModelAdmin):
    inlines = [ReObjectImageInline]
    list_display = [
        "photos_main",
        "id",
        "category",
        "type_house",
        "number_of_storeys",
        "floor",
        "number_of_rooms",
        "total_area",
        "living_area",
        "kitchen_area",
        "windows_orientation",
        "ownership",
        "land_category",
        "land_area",
        "relief_area",
        "fencing",
        "foundation",
        "wall_material",
        "buildings_on_site",
        "buildings_of_villages",
        "village_fences",
        "object_description",
    ]  # Customize as needed

    readonly_fields = ("preview_photo", "photos_main")

    def photos(self, obj):
        photos = obj.photos.all().values_list("image", flat=True)
        return ", ".join(str(photo) for photo in photos)

    def photos_main(self, obj):
        photos = obj.photos.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" height="50"/>'.format(photos[0].image.url)
            )
        return "avatar"

    photos.short_description = "Photos"
    photos_main.short_description = "Photo"

    def preview_photo(self, obj):
        """for local"""
        photos = obj.photos.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(photo.image.url)
                for photo in photos
            )
        )

    preview_photo.short_description = "Photo Preview"
