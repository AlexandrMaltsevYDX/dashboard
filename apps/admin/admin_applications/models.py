from django.db import models

from apps.applications.models.application import Application


# Create your models here.
class ApplicationProxy(Application):
    def __str__(self):
        return f"{self.applicant}"

    class Meta:
        proxy = True
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"
