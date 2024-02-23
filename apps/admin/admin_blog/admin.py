from django.contrib import admin
from django.utils.html import format_html

from apps.blog import models
from .models import PostProxy


# Register your models here.
class PostImageInline(admin.TabularInline):
    model = models.posts.PostImageModel
    extra = 1
    fields = ("image", "uuid")
    exclude = ("uuid",)


class PostTagsInline(admin.StackedInline):
    model = models.posts.PostTagsModel
    extra = 1
    fields = ("tag", "uuid")
    exclude = ("uuid",)


@admin.register(PostProxy)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, PostTagsInline]
    readonly_fields = [
        "photo",
        "tags_display",
    ]
    list_display = ("name", "photo", "tags_display")
    list_filter = [
        "author",
    ]

    def photo(self, obj):
        photos = obj.postimages.all()
        if len(photos) > 0:
            return format_html(
                '<img src="{}" height="50"/>'.format(photos[0].image.url)
            )
        return "Photo"

    def tags_display(self, obj):
        post_tags = obj.posts_posts.all().values_list("tag__name", flat=True)
        return ", ".join(post_tags)

    photo.short_description = "Photo"
    tags_display.short_description = "Tags"
