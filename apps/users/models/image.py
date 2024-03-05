from django.db import models

from apps.core.models.base import BaseModel, BaseImageModel
from apps.users.models.profile import EmployeeProfileModel


class EmployeeProfileAvatarModel(BaseImageModel):
    objectModel = models.ForeignKey(
        EmployeeProfileModel,
        related_name="avatars",
        on_delete=models.CASCADE,
    )
    image = models.FileField(upload_to="avatars/")

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Фото Сотрудника"
        verbose_name_plural = "Фото Сотрудников"
