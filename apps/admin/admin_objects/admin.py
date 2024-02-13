from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import ReObjectProxy, ReObjectImageProxy, ReObjectEngineeringServicesProxy
from django.templatetags.static import static
from apps.reobjects import models


class ReObjectPlanModelInline(admin.TabularInline):
    model = models.objects_re.ReObjectPlanModel
    extra = 1
    # fields = ("image", "uuid")
    # exclude = ("uuid",)


class ReObjectImageProxyInline(admin.TabularInline):
    model = models.objects_re.ReObjectImage
    extra = 1
    # fields = ("image", "uuid")
    # exclude = ("uuid",)


class ReObjectEmploeeProxyInline(admin.TabularInline):
    model = models.objects_re.ReObjectEmployee
    extra = 1
    # readonly_fields = ("tag", "text")


class ReObjectEngineeringServicesProxyInline(admin.TabularInline):
    model = ReObjectEngineeringServicesProxy
    extra = 1
    readonly_fields = ("tag", "text")

    # exclude = ("uuid",)
    @admin.display(description="tag")
    def tag(self, obj):
        # q = self.model.engineering_service
        q = obj.engineering_service.tag
        return f"{q}"

    @admin.display(description="text")
    def text(self, obj):
        # q = self.model.engineering_service
        q = obj.engineering_service.text
        return f"{q}"


@admin.register(ReObjectProxy)
class ReObjectProxyModel(admin.ModelAdmin):
    inlines = [
        ReObjectImageProxyInline,
        ReObjectPlanModelInline,
        ReObjectEngineeringServicesProxyInline,
        ReObjectEmploeeProxyInline,
    ]
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
        "village_fences",
        "display_engineering_services",
        "object_description",
        "coordinates",
    ]  # Customize as needed
    # exclude = ("uuid",)

    readonly_fields = (
        "photo_images",
        "plans_images",
        "display_engineering_services",
        "display_agents",
    )

    def display_engineering_services(self, obj):
        engineering_services = obj.re_objects.all().values_list(
            "engineering_service__name", flat=True
        )
        return ", ".join(engineering_services)

    def display_agents(self, obj):
        # agents = obj.reobjectemployees.all().values_list(
        #     "employee__username", flat=True
        # )
        agents = [
            f"{i.employee.first_name} {i.employee.last_name}"
            for i in obj.reobjectemployees.all()
        ]
        print(agents)
        return ", ".join(agents)

    def photos_main(self, obj):
        photos = obj.photos.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" alt="{}" height="50"/>'.format(
                    photos[0].image.url, photos[0].image.url
                )
            )
        return "avatar"

    def plans_images(self, obj):
        """for local"""
        plans = obj.reobjectplans.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(plan.image.url) for plan in plans
            )
        )

    def photo_images(self, obj):
        """for local"""
        photos = obj.photos.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(photo.image.url)
                for photo in photos
            )
        )

    photo_images.short_description = "Фотографии объекта"
    plans_images.short_description = "Планы объекта"
    photos_main.short_description = "Первое фото"
    display_engineering_services.short_description = "Инженерные коммуникации"
    display_agents.short_description = "Агенты"

    class Media:
        js = [static("test.js")]


# Register your models here.
