from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import ReObjectProxy, ReObjectImageProxy, ReObjectEngineeringServicesProxy
from django.templatetags.static import static
from apps.reobjects import models


class ReObjectPlanModelInline(admin.TabularInline):
    model = models.objects_re.ReObjectPlanModel
    extra = 1
    ordering = ("order",)
    # fields = ("image", "uuid")
    # exclude = ("uuid",)


class ReObjectImageProxyInline(admin.TabularInline):
    model = models.objects_re.ReObjectImage
    extra = 1
    ordering = ("order",)
    # readonly_fields = ("order",)

    # @admin.display(description="order")
    # def order(self, obj):
    #     # q = self.model.engineering_service
    #     q = obj.image.order
    #     print()
    #     return f"{q}"

    # fields = ("image", "uuid")
    # exclude = ("uuid",)


class ReObjectEmploeeProxyInline(admin.TabularInline):
    model = models.objects_re.ReObjectEmployee
    extra = 1
    # readonly_fields = ("tag", "text")


class ReObjectCloseProxyInline(admin.TabularInline):
    model = models.objects_re.ReObjectClose
    extra = 1
    fk_name = "re_object"
    # readonly_fields = ("tag", "text")


class ReObjectVisibleObSiteProxyInline(admin.TabularInline):
    model = models.objects_re.ReObjectVisibleOnSite
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
    list_filter = [
        # "visible_on_site",
        "category",
        "repair__name",
    ]

    search_fields = [
        "name",
        "category__name",
        "place",
        "metro",
        "land_category__value",
        "approve_usage__value",
        "ownership__value",
        "repair__name",
        "balcony__name",
        "sales_method__name",
        "type_house__name",
        "foundation__value",
        "wall_material__value",
        "object_description",
    ]

    # raw_id_fields = [
    #     "category",
    # ]

    inlines = [
        ReObjectImageProxyInline,
        ReObjectPlanModelInline,
        ReObjectEngineeringServicesProxyInline,
        ReObjectEmploeeProxyInline,
        ReObjectVisibleObSiteProxyInline,
        ReObjectCloseProxyInline,
    ]
    list_display = [
        "photos_main",
        "id",
        "name",
        "category",
        # "visible_on_site",
    ]  # Customize as needed
    # exclude = ("uuid",)

    readonly_fields = (
        "photo_images",
        "plans_images",
        "display_engineering_services",
        "display_agents",
        "display_pages",
        "display_close",
    )

    fields = [
        "id",
        # "visible_on_site",
        "name",
        "category",
        "place",
        "distance_CAD",
        "metro",
        "land_category",
        "approve_usage",
        "ownership",
        "area_house",
        "land_area_measurement",
        "area_plot",
        "area_flat",
        "living_area",
        "kitchen_area",
        "area_room",
        "number_of_rooms",
        "number_of_storeys",
        "floor",
        "window_material",
        "windows_orientation",
        "ceiling_height",
        "repair",
        "wc",
        "balcony",
        "sales_method",
        "type_house",
        "date_foundation",
        "lift",
        "foundation",
        "wall_material",
        "price",
        "relief_area",
        "fencing",
        "buildings_on_plot",
        "driveways",
        "village_fences",
        "object_description",
        # "coordinates",
        "yandex_map_link",
        "date_sale",
        "you_tube_link",
        "display_engineering_services",
        "display_agents",
        "plans_images",
        "photo_images",
        "display_pages",
        "display_close",
    ]

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
        return ", ".join(agents)

    def display_close(self, obj):
        # agents = obj.reobjectemployees.all().values_list(
        #     "employee__username", flat=True
        # )
        closes = [f"ID-{i.close_re_object.id}" for i in obj.reobjectbase.all()]
        return ", ".join(closes)

    def display_pages(self, obj):
        # agents = obj.reobjectemployees.all().values_list(
        #     "employee__username", flat=True
        # )
        pages = [f"{i.page.value}" for i in obj.reobjectsite.all()]
        return ", ".join(pages)

    def photos_main(self, obj):
        photos = obj.photo_images.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" alt="{}" height="50"/>'.format(
                    photos[0].image.url, photos[0].image.url
                )
            )
        return "avatar"

    def plans_images(self, obj):
        """for local"""
        plans = obj.plans_images.all()

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
    display_pages.short_description = "Отображение на сайте"
    display_close.short_description = "Похожие объекты"
