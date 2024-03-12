from django.db.models import (
    ForeignKey,
    IntegerField,
    PositiveIntegerField,
    FloatField,
    CharField,
    TextField,
    CASCADE,
    RESTRICT,
    OneToOneField,
    BooleanField,
    PositiveBigIntegerField,
)

from mdeditor.fields import MDTextField
from apps.core.models.base import BaseModel, TimeStampedModel
from apps.village.models import attributes
from apps.reobjects.models import attributes as house_attributes


class Village(TimeStampedModel, BaseModel):
    id = IntegerField(
        blank=True,
        null=True,
        verbose_name="ID посёлка",
    )

    visible_on_site = BooleanField(
        blank=True,
        null=True,
        verbose_name="Отображать на сайте",
    )

    name = TextField(
        verbose_name="Название объекта",
        help_text="Введите текст",
        blank=True,
        null=True,
    )

    place = TextField(
        max_length=255,
        verbose_name="Адрес",
        help_text="Введите текст",
        blank=True,
        null=True,
    )

    infra = TextField(
        verbose_name="Инфраструктура",
        help_text="Введите текст",
        blank=True,
        null=True,
    )

    distance_CAD = FloatField(
        null=True,
        blank=True,
        verbose_name="Расстояние до кад",
        help_text="введите знaчение в КМ, например '1.2' ",
    )
    area_of_houses = TextField(
        null=True,
        blank=True,
        verbose_name="Площадь домов в кв.м",
        help_text="введите знaчение, например '100 - 200' ",
    )

    wall_material = ForeignKey(
        house_attributes.WallMaterial,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Материал стен домов в поселке",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    buildings_of_villages = PositiveIntegerField(
        verbose_name="Количество объектов в поселке",
        help_text="Количество объектов в поселке",
        null=True,
        blank=True,
    )

    foundation = ForeignKey(
        house_attributes.Foundation,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Фундамент домов",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    area_of_plot = FloatField(
        null=True,
        blank=True,
        verbose_name="Площадь одного участка",
        help_text="введите знaчение, например '1.2' ",
    )

    area_of_plot_measurement = ForeignKey(
        attributes.AreaOfPlotMeasurement,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Единица измерения площади одного участка",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    category_land = ForeignKey(
        attributes.CategoryLandPlot,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Категория земель участков",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    relief_area_plot = ForeignKey(
        attributes.ReliefAreaPlot,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Рельеф участков",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    fencing_village = ForeignKey(
        attributes.FencingVillage,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Ограждение поселка",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    security_village = ForeignKey(
        attributes.SecurityVillage,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Охрана поселка",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    object_description = MDTextField(
        null=True,
        blank=True,
        verbose_name="Описание объекта",
        help_text="Текст с форматированием",
    )

    buildings_on_plot = TextField(
        verbose_name="Строения на участке",
        help_text="Опишите строения на участке",
        blank=True,
        null=True,
    )

    you_tube_link = TextField(
        verbose_name="Ссылка на YouTube",
        help_text="скопируйте ссылку из браузера и вставьте в это поле",
        blank=True,
        null=True,
    )

    yandex_map_link = TextField(
        verbose_name="Ссылка на YandexMap",
        help_text="скопируйте ссылку iframe из браузера и вставьте в это поле",
        blank=True,
        null=True,
    )

    price = PositiveBigIntegerField(
        null=True,
        blank=True,
        verbose_name="Цена",
        help_text="введите знaчение в РУБ, например '1000000' ",
    )
