from django.db import models

from apps.core.models.base import BaseModel, BaseImageModel
from apps.users.models.profile import EmployeeProfileModel
from apps.users.models.re_object import ReObjectModel


class EmployeeProfileAvatarModel(BaseImageModel):
    profile = models.ForeignKey(
        EmployeeProfileModel,
        related_name="avatars",
        on_delete=models.CASCADE,
    )
    image = models.FileField(upload_to="avatars/")

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Аватар Сотрудника"
        verbose_name_plural = "Аватары Сотрудников"


class ReObjectImageModel(BaseImageModel):
    re_object = models.ForeignKey(
        ReObjectModel,
        related_name="reobject_images",
        on_delete=models.CASCADE,
    )
    image = models.FileField(upload_to="avatars/")

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Картинка Объекта недвижимости"
        verbose_name_plural = "Картинки Объектов недвижимости"
