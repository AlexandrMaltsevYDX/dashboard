from django.db.models import CharField, TextField, ForeignKey, CASCADE
from apps.core.models.base import BaseModel
from mdeditor.fields import MDTextField
from apps.users.models import EmployeeProfileModel


class Post(BaseModel):
    name = TextField(
        max_length=255,
        verbose_name="Название поста",
        help_text="Введите текст",
        blank=True,
    )
    author = ForeignKey(
        EmployeeProfileModel,
        on_delete=CASCADE,
        verbose_name="Автор поста",
        null=True,
        blank=True,
    )

    body = MDTextField(
        null=True,
        blank=True,
        verbose_name="Текст с форматированием",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["author"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
