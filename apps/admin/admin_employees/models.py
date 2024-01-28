from apps.users.models import (
    EmployeeProfileModel,
    EmployeeProfileAvatarModel,
)


# Create your models here.
class EmployeeProfileProxyModel(EmployeeProfileModel):
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        proxy = True
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


# class EmployeeImageProxyModel(EmployeeProfileAvatarModel):
#     def __str__(self):
#         return f"{self.image}"
#
#     class Meta:
#         proxy = True
#         verbose_name = "Аватар"
#         verbose_name_plural = "Аватары"
