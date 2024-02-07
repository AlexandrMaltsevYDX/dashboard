from django.contrib import admin
from django.utils.html import format_html

from apps.applications import models
from .models import ApplicationProxy


# Register your models here.
class ApplicationImageModelInline(admin.TabularInline):
    model = models.application.ApplicationImageModel
    extra = 1
    fields = ("image", "uuid")
    exclude = ("uuid",)


# Register your models here.


@admin.register(ApplicationProxy)
class ApplicationAdmin(admin.ModelAdmin):
    inlines = [ApplicationImageModelInline]
    readonly_fields = [
        "photo",
    ]
    list_display = (
        "applicant",
        "contact",
        "created_at",
        "photo",
        "text",
    )
    list_filter = [
        "created_at",
    ]

    def photo(self, obj):
        photos = obj.applicationimages.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" height="50"/>'.format(photos[0].image.url)
            )
        return "Photo"

    photo.short_description = "Photo"
