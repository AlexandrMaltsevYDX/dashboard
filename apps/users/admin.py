from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group as BaseGroup
from django.utils.html import format_html
from django.conf import settings

from apps.users.models import (
    User,
    Group,
    EmployeeProfileModel,
    EmployeeProfileAvatarModel,
)


class AvatarsInline(admin.TabularInline):
    model = EmployeeProfileAvatarModel
    extra = 1


@admin.register(EmployeeProfileModel)
class EmployeeProfileModelAdmin(admin.ModelAdmin):
    inlines = [AvatarsInline]
    list_display = [
        "user",
        "username",
        "first_name",
        "last_name",
        "description",
        "avatars",
    ]  # Customize as needed

    readonly_fields = ("preview_avatar",)
    fieldsets = [
        (
            "Profile Details",
            {
                "fields": [
                    "user",
                    "username",
                    "first_name",
                    "last_name",
                    "description",
                    "preview_avatar",
                ]
            },
        ),
    ]

    def avatars(self, obj):
        avatars = obj.employeeprofileavatarmodel_set.all().values_list(
            "image", flat=True
        )
        return ", ".join(str(avatar) for avatar in avatars)

    avatars.short_description = "Avatars"

    def preview_avatar(self, obj):
        """for local"""
        avatars = obj.employeeprofileavatarmodel_set.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(avatar.image.url)
                for avatar in avatars
            )
        )

    preview_avatar.short_description = "Avatar Preview"

    def save_model(self, request, obj, form, change):
        # Automatically populate fields based on associated User
        obj.username = obj.user.username
        obj.first_name = obj.user.first_name
        obj.last_name = obj.user.last_name

        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)


admin.site.unregister(BaseGroup)
