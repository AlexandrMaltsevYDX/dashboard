from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import VillageProxy
from django.templatetags.static import static
from apps.village import models


class ReObjectCloseProxyInline(admin.TabularInline):
    model = models.relationships.ReObjectInVillages
    extra = 1
    # fk_name = "villagebase"
    # readonly_fields = ("tag", "text")


class VillageImageModelProxyInline(admin.TabularInline):
    model = models.village.VillageImageModel
    extra = 1
    ordering = ("order",)
    # fields = ("image", "uuid")
    # exclude = ("uuid",)


class VillagePlanModelProxyInline(admin.TabularInline):
    model = models.village.VillagePlanModel
    extra = 1
    ordering = ("order",)
    # fields = ("image", "uuid")
    # exclude = ("uuid",)


class VillageEmployeeProxyInline(admin.TabularInline):
    model = models.relationships.VillageEmployee
    extra = 1
    # readonly_fields = ("tag", "text")


class VillageEngineeringServicesProxyInline(admin.TabularInline):
    model = models.relationships.VillageEngineeringServices
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


@admin.register(VillageProxy)
class VillageProxyModel(admin.ModelAdmin):
    inlines = [
        VillageImageModelProxyInline,
        VillagePlanModelProxyInline,
        VillageEngineeringServicesProxyInline,
        VillageEmployeeProxyInline,
        ReObjectCloseProxyInline,
    ]
    list_display = [
        "id",
        "name",
        "object_description",
    ]  # Customize as needed
    # exclude = ("uuid",)

    readonly_fields = (
        "images_village",
        "plans_village",
        "display_engineering_services",
        "display_agents",
        "display_reobject",
    )

    def first_image(self, obj):
        photos = obj.villageimages.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" alt="{}" height="50"/>'.format(
                    photos[0].image.url, photos[0].image.url
                )
            )
        return "avatar"

    def images_village(self, obj):
        """for local"""
        photos = obj.villageimages.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(photo.image.url)
                for photo in photos
            )
        )

    def first_plan(self, obj):
        photos = obj.villageplans.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" alt="{}" height="50"/>'.format(
                    photos[0].image.url, photos[0].image.url
                )
            )
        return "avatar"

    def plans_village(self, obj):
        """for local"""
        photos = obj.villageplans.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(photo.image.url)
                for photo in photos
            )
        )

    def display_engineering_services(self, obj):
        village_engineering_services = obj.villages.all().values_list(
            "engineering_service__name", flat=True
        )
        return ", ".join(village_engineering_services)

    def display_agents(self, obj):
        agents = [
            f"{i.employee.first_name} {i.employee.last_name}"
            for i in obj.villageemployees.all()
        ]
        print(agents)
        return ", ".join(agents)

    def display_reobject(self, obj):
        objectsinvillages = [
            f"ID-{i.re_object_in_villages.id}" for i in obj.villagebase.all()
        ]
        print(objectsinvillages)
        return ", ".join(objectsinvillages)

    first_image.short_description = "Первая фотография объекта"
    images_village.short_description = "Фото объектов"
    first_plan.short_description = "Первый план объекта"
    plans_village.short_description = "Планы объектов"
    display_engineering_services.short_description = "Инженерные коммуникации"
    display_agents.short_description = "Агенты"
    display_reobject.short_description = "Объекты в поселках"
