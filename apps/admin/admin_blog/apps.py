from django.apps import AppConfig


class AdminBlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.admin.admin_blog"
    label = "apps_admin_blog"
    verbose_name = "04. Блог"
