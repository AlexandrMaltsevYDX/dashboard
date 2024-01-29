from django.apps import AppConfig


class AdminObjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.admin.admin_objects"
    label = "apps_admin_objects"
    verbose_name = "01. Объекты"
