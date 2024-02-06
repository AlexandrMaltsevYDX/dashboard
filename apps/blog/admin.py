from django.contrib import admin
from django.utils.html import format_html
from . import models


admin.site.register(models.posts.Tag)
admin.site.register(models.posts.PostTagsModel)
admin.site.register(models.posts.PostImageModel)
#
#
# class PostImageInline(admin.TabularInline):
#     model = models.posts.PostImageModel
#     extra = 1
#     fields = ("image", "uuid")
#     exclude = ("uuid",)
#
#
# class PostTagsInline(admin.StackedInline):
#     model = models.posts.PostTagsModel
#     extra = 1
#     fields = ("tag", "uuid")
#     exclude = ("uuid",)
#
#
# @admin.register(models.posts.Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageInline, PostTagsInline]
#     readonly_fields = [
#         "photo",
#         "tags_display",
#     ]
#     list_display = ("name", "photo", "tags_display")
#
#     def photo(self, obj):
#         photos = obj.postimages.all()
#         if len(photos) > 0:
#             return format_html(
#                 '<img src="{}" height="50"/>'.format(photos[0].image.url)
#             )
#         return "Photo"
#
#     def tags_display(self, obj):
#         post_tags = obj.posts.all().values_list("tag__name", flat=True)
#         return ", ".join(post_tags)
#
#     photo.short_description = "Photo"
#     tags_display.short_description = "Tags"
