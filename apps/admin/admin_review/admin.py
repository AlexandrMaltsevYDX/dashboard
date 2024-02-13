from django.contrib import admin
from django.utils.html import format_html

from apps.reviews import models
from .models import ReviewProxy


# Register your models here.
class ReviewImageInline(admin.TabularInline):
    model = models.review.ReviewImageModel
    extra = 1
    fields = ("image", "uuid")
    exclude = ("uuid",)


@admin.register(ReviewProxy)
class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewImageInline]
    readonly_fields = [
        "photo",
    ]
    list_display = (
        "author_name",
        "created_at",
        "photo",
        "link_to_src",
    )
    list_filter = [
        "date_sale",
    ]

    def photo(self, obj):
        photos = obj.reviewimages.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" height="50"/>'.format(photos[0].image.url)
            )
        return "Photo"

    photo.short_description = "Photo"
