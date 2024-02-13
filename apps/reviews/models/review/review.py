from django.db.models import CharField, DateField
from mdeditor.fields import MDTextField
from apps.core.models.base import BaseModel, TimeStampedModel


class Review(TimeStampedModel, BaseModel):
    text = MDTextField(
        null=True,
        blank=True,
        verbose_name="Текст с форматированием",
    )
    author_name = CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Имя автора полностью",
        help_text="например: Андреева Любовь, Кох И.С.",
    )
    link_to_src = CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Ccылка на источник",
        help_text="Скопируйте ссылку отзыва и поместите в это поле",
    )

    date_sale = DateField(
        verbose_name="Дата публикации",
        help_text="Выберите дату публикации",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
