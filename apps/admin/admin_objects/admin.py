from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import ReObjectProxy, ReObjectImageProxy, ReObjectEngineeringServicesProxy
from django.templatetags.static import static


class ReObjectImageProxyInline(admin.TabularInline):
    model = ReObjectImageProxy
    extra = 1
    # fields = ("image", "uuid")
    # exclude = ("uuid",)


class ReObjectEngineeringServicesProxyInline(admin.TabularInline):
    model = ReObjectEngineeringServicesProxy
    extra = 1
    # fields = ("engineering_service", "uuid")
    # exclude = ("uuid",)


@admin.register(ReObjectProxy)
class ReObjectProxyModel(admin.ModelAdmin):
    inlines = [ReObjectImageProxyInline, ReObjectEngineeringServicesProxyInline]
    list_display = [
        "photos_main",
        "id",
        "name",
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
        "buildings_of_villages",
        "village_fences",
        "display_engineering_services",
        "object_description",
        "coordinates",
    ]  # Customize as needed
    # exclude = ("uuid",)

    readonly_fields = ("preview_photo", "photos_main", "display_engineering_services")

    def photos(self, obj):
        photos = obj.photos.all().values_list("image", flat=True)
        return ", ".join(str(photo) for photo in photos)

    def photos_main(self, obj):
        photos = obj.photos.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" alt="{}" height="50"/>'.format(
                    photos[0].image.url, photos[0].image.url
                )
            )
        return "avatar"

    def display_engineering_services(self, obj):
        engineering_services = obj.re_objects.all().values_list(
            "engineering_service__value", flat=True
        )
        return ", ".join(engineering_services)

    photos.short_description = "Фотографии объекта"
    photos_main.short_description = "Первое фото"
    display_engineering_services.short_description = "Инженерные коммуникации"

    def preview_photo(self, obj):
        """for local"""
        photos = obj.photos.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(photo.image.url)
                for photo in photos
            )
        )

    preview_photo.short_description = "Фотографии объекта"

    class Media:
        js = [static("test.js")]


# Register your models here.
