from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.core.models.base import BaseModel, TimeStampedModel
from .user import User
from .jobtitle import JobTitle


class EmployeeProfileModel(TimeStampedModel, BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Фамилия",
    )

    work_email = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Рабочий Email",
    )
    phone_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Номе телефона",
    )
    telegram_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Telegram",
    )
    whatsapp_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Whatsapp",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )

    job_title = models.ForeignKey(
        JobTitle,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        verbose_name="Должность",
    )

    location = models.TextField(
        blank=True,
        null=True,
        verbose_name="Район, Районы",
    )

    def save(self, *args, **kwargs):
        self.username = self.user.username
        self.first_name = self.user.first_name
        self.last_name = self.user.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


@receiver(post_save, sender=User)
def create_or_update_employee_profile(sender, instance, created, **kwargs):
    try:
        employee_profile = instance.employeeprofilemodel
    except EmployeeProfileModel.DoesNotExist:
        employee_profile = None

    if created or not employee_profile:
        # If the User is created or no associated EmployeeProfileModel exists, create a new one.
        EmployeeProfileModel.objects.create(user=instance)
    else:
        # If an associated EmployeeProfileModel exists, update it with new data.
        employee_profile.username = instance.username
        employee_profile.first_name = instance.first_name
        employee_profile.last_name = instance.last_name
        employee_profile.save()
