from django.db.models import CharField, TextField
from apps.core.models.base import BaseModel, TimeStampedModel


class Application(TimeStampedModel, BaseModel):
    text = TextField(
        blank=True,
        null=True,
        verbose_name="Текст вопроса",
        help_text="Просто текст",
    )
    applicant = CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Имя покупателя полностью",
        help_text="например: Андреева Любовь, Кох И.С.",
    )
    contact = TextField(
        blank=True,
        null=True,
        verbose_name="Контактные данные",
        help_text="Контактные данные",
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
