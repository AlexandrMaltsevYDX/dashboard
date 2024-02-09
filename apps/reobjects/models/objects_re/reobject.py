from django.db.models import (
    ForeignKey,
    IntegerField,
    PositiveIntegerField,
    FloatField,
    TextField,
    CASCADE,
    RESTRICT,
    OneToOneField,
    PositiveBigIntegerField,
    DateField,
)
from mdeditor.fields import MDTextField
from apps.core.models.base import BaseModel, TimeStampedModel
from apps.reobjects import models


# Create your models here.
class ReObject(TimeStampedModel, BaseModel):
    id = IntegerField(
        blank=True,
        null=True,
    )

    name = TextField(
        max_length=255,
        verbose_name="Название объекта",
        help_text="Адрес",
        blank=True,
        null=True,
    )

    date_sale = DateField(
        verbose_name="Дата продажи",
        help_text="введите дату",
        blank=True,
        null=True,
    )

    balcony = ForeignKey(
        models.attributes.Balcony,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Тип балкона/лоджии",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    wc = TextField(
        max_length=255,
        verbose_name="Санузел",
        help_text="Введите текст",
        blank=True,
        null=True,
    )

    category = ForeignKey(
        models.attributes.Category,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Категория объекта",
        help_text="Дом, Квартира, Участок",
    )

    type_house = ForeignKey(
        models.attributes.TypeHouse,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Тип объекта",
        help_text="Комерческая, ИЖС, Жилая",
    )

    number_of_storeys = PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Этажность",
        help_text="Количество этажей в здании",
    )

    floor = PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Этаж",
        help_text="Этаж в здании",
    )

    number_of_rooms = PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Количество комнат",
        help_text="Количество комнат в помещении",
    )

    total_area = FloatField(
        null=True,
        blank=True,
        verbose_name="Общая площадь помещений",
        help_text="Общая площадь помещений",
    )

    ceiling_height = FloatField(
        null=True,
        blank=True,
        verbose_name="Высота потолков",
        help_text="Ведите цифры в метрах например '3.2'",
    )

    living_area = FloatField(
        null=True,
        blank=True,
        verbose_name="Жилая площадь",
        help_text="Жилая площадь в помещении",
    )

    kitchen_area = FloatField(
        null=True,
        blank=True,
        verbose_name="Площадь кухни",
        help_text="Площадь кухни в помещении",
    )

    windows_orientation = ForeignKey(
        models.attributes.WindowsOrientation,
        on_delete=CASCADE,
        null=True,
        verbose_name="Ориентация окон",
        help_text="Запад, Север, Восток, и.т.д",
        blank=True,
    )

    ownership = ForeignKey(
        models.attributes.Ownership,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Собственность",
        help_text="От собственника, Ипотека, и.т.д",
    )

    land_category = ForeignKey(
        models.attributes.LandCategory,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Категория земель",
        help_text="Коммерческая",
    )

    land_area_measurement = ForeignKey(
        models.attributes.AreaOfMeasurement,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Единицы измерения площади участка",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    land_area = FloatField(
        verbose_name="Площадь участка",
        help_text="Площадь участка",
        null=True,
        blank=True,
    )

    relief_area = ForeignKey(
        models.attributes.ReliefArea,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Рельеф участка",
        help_text="Горы, Холмы",
    )

    distance_CAD = FloatField(
        null=True,
        blank=True,
        verbose_name="Расстояние до кад",
        help_text="введите знaчение в КМ, например '1.2' ",
    )

    price = PositiveBigIntegerField(
        null=True,
        blank=True,
        verbose_name="Цена",
        help_text="введите знaчение в РУБ, например '1000000' ",
    )

    repair = ForeignKey(
        models.attributes.Repair,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Ремонт",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    fencing = ForeignKey(
        models.attributes.Fencing,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Ограждение",
        help_text="Горы, Шморы",
    )

    foundation = ForeignKey(
        models.attributes.Foundation,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Фундамент",
        help_text="Блоки, Лента, Плита",
    )

    wall_material = ForeignKey(
        models.attributes.WallMaterial,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Материал стен",
        help_text="Кирпич, Панель, Пеноблок",
    )

    village_fences = ForeignKey(
        models.attributes.VillageFences,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Ограждение поселка",
        help_text="Да, нет",
    )

    object_description = MDTextField(
        null=True,
        blank=True,
        verbose_name="Описание объекта",
        help_text="Текст с форматированием",
    )

    coordinates = OneToOneField(
        models.attributes.Coordinates,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Координаты объекта",
        help_text="Широта, Долгота",
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

    driveways = ForeignKey(
        models.attributes.Driveways,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Подъездные пути",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    class Meta:
        verbose_name = "Объекты недвижимости"
        verbose_name_plural = "Объекты недвижимости"
