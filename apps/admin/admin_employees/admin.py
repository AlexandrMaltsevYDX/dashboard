from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import EmployeeProfileProxyModel, EmployeeProfileAvatarModel

# Register your models here.


class AvatarsProxyInline(admin.TabularInline):
    model = EmployeeProfileAvatarModel
    extra = 1
    fields = ("image", "uuid")
    exclude = ("uuid",)


@admin.register(EmployeeProfileProxyModel)
class EmployeeProfileProxyModel(admin.ModelAdmin):
    inlines = [AvatarsProxyInline]
    list_display = [
        "avatar_main",
        # "avatars",
        "first_name",
        "last_name",
        "job_title",
        "work_email",
        "phone_number",
        "telegram_link",
        "whatsapp_link",
        # "description",
    ]  # Customize as needed

    readonly_fields = ("preview_avatar",)
    # fieldsets = [
    #     (
    #         "Profile Details",
    #         {
    #             "fields": [
    #                 "uuid",
    #                 "last_name",
    #                 "position",
    #                 "work_email",
    #                 "phone_number",
    #                 "telegram_link",
    #                 "whatsapp_link",
    #                 "description",
    #                 "preview_avatar",
    #             ]
    #         },
    #     ),
    # ]

    def avatars(self, obj):
        avatars = obj.avatars.all().values_list("image", flat=True)
        return ", ".join(str(avatar) for avatar in avatars)

    def avatar_main(self, obj):
        avatars = obj.avatars.all()
        if len(avatars) > 0:
            return format_html(
                '<img src="{}" height="50"/>'.format(avatars[0].image.url)
            )
        return "avatar"

    avatars.short_description = "Avatars"
    avatar_main.short_description = "Avatar"

    def preview_avatar(self, obj):
        """for local"""
        avatars = obj.avatars.all()

        return format_html(
            "<br>".join(
                '<img src="{}" height="50"/>'.format(avatar.image.url)
                for avatar in avatars
            )
        )

    preview_avatar.short_description = "Фото сотрудника"

    def save_model(self, request, obj, form, change):
        # Automatically populate fields based on associated User
        obj.username = obj.user.username
        obj.first_name = obj.user.first_name
        obj.last_name = obj.user.last_name

        super().save_model(request, obj, form, change)
