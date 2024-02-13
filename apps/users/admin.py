from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group as BaseGroup
from django.utils.html import format_html
from django.conf import settings

from apps.users.models import (
    User,
    Group,
    JobTitle,
)

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.unregister(BaseGroup)
admin.site.register(JobTitle)
