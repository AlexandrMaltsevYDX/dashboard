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
    BooleanField,
)
from mdeditor.fields import MDTextField
from apps.core.models.base import BaseModel, TimeStampedModel
from apps.reobjects import models


# Create your models here.
class ReObject(TimeStampedModel, BaseModel):
    id = PositiveBigIntegerField(
        # blank=True,
        # null=True,
        # default=0,
        unique=True,
        verbose_name="ID объекта",
    )

    name = TextField(
        max_length=255,
        verbose_name="Название объекта",
        help_text="Название объекта",
        blank=True,
        null=True,
    )

    category = ForeignKey(
        models.attributes.Category,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Категория объекта",
        help_text="Дом, Квартира, Участок",
    )

    place = TextField(
        max_length=255,
        verbose_name="Адрес",
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

    metro = TextField(
        verbose_name="Метро",
        help_text="Академическая, 5 мин. Пешком, 15 мин. транспорт",
        blank=True,
        null=True,
    )

    land_category = ForeignKey(
        models.attributes.LandCategory,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Категория земель",
        help_text="Коммерческая",
    )

    approve_usage = ForeignKey(
        models.attributes.ApproveUsage,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Разрешенное использование",
        help_text="Разрешенное использование",
    )

    ownership = ForeignKey(
        models.attributes.Ownership,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Собственность",
        help_text="От собственника, Ипотека, и.т.д",
    )

    area_house = FloatField(
        null=True,
        blank=True,
        verbose_name="Площадь дома, кв. м",
        help_text="Площадь дома, кв. м",
    )

    land_area_measurement = ForeignKey(
        models.attributes.AreaOfMeasurement,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Единицы измерения площади участка",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    area_plot = FloatField(
        null=True,
        blank=True,
        verbose_name="Площадь участка",
        help_text="Единицы измерения, Площадь участка, кв. м, сотки - выбираются выше",
    )

    area_flat = FloatField(
        null=True,
        blank=True,
        verbose_name="Общая площадь, кв. м",
        # help_text="Площадь квартиры общая, кв. м",
    )

    living_area = FloatField(
        null=True,
        blank=True,
        verbose_name="Жилая площадь, кв. м",
        help_text="Жилая площадь в помещении",
    )

    kitchen_area = FloatField(
        null=True,
        blank=True,
        verbose_name="Площадь кухни, кв. м",
        help_text="Площадь кухни в помещении",
    )

    area_room = FloatField(
        null=True,
        blank=True,
        verbose_name="Площадь комнаты, кв. м",
        help_text="Для коммунальных квартир",
    )

    number_of_rooms = PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Количество комнат",
        help_text="Количество комнат в помещении",
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

    window_material = ForeignKey(
        models.attributes.WindowMaterial,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Материал окон",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    windows_orientation = ForeignKey(
        models.attributes.WindowsOrientation,
        on_delete=RESTRICT,
        null=True,
        verbose_name="Ориентация окон",
        help_text="Запад, Север, Восток, и.т.д",
        blank=True,
    )

    ceiling_height = FloatField(
        null=True,
        blank=True,
        verbose_name="Высота потолков",
        help_text="Ведите цифры в метрах например '3.2'",
    )

    repair = ForeignKey(
        models.attributes.Repair,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Ремонт",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    wc = ForeignKey(
        models.attributes.WC,
        on_delete=RESTRICT,
        verbose_name="Санузел",
        help_text="Выберите из списка, или создайте новое '+'",
        blank=True,
        null=True,
    )

    balcony = ForeignKey(
        models.attributes.Balcony,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Тип балкона/лоджии",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    sales_method = ForeignKey(
        models.attributes.SalesMethod,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Способ продажи",
        help_text="Выберете значение из списка, или создайте новое '+'",
    )

    type_house = ForeignKey(
        models.attributes.TypeHouse,
        on_delete=CASCADE,
        null=True,
        blank=True,
        verbose_name="Тип объекта",
        help_text="Вторичное жилье, Новостройка... Выберите из списка, или создайте новое '+'",
    )

    date_foundation = PositiveIntegerField(
        verbose_name="Год постройки дома",
        help_text="введите дату",
        blank=True,
        null=True,
    )

    lift = ForeignKey(
        models.attributes.Lift,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Лифт",
        help_text="да, нет, 2, 3, 4",
    )

    foundation = ForeignKey(
        models.attributes.Foundation,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Фундамент",
        help_text="Блоки, Лента, Плита ... Выберите из списка, или создайте новое '+'",
    )

    wall_material = ForeignKey(
        models.attributes.WallMaterial,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Материал стен",
        help_text="Кирпич, Панель, Пеноблок ... Выберите из списка, или создайте новое '+'",
    )

    price = PositiveBigIntegerField(
        null=True,
        blank=True,
        verbose_name="Цена",
        help_text="введите знaчение в РУБ, например '1000000' ",
    )

    relief_area = ForeignKey(
        models.attributes.ReliefArea,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Рельеф участка",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    fencing = ForeignKey(
        models.attributes.Fencing,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Ограждение участка",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    buildings_on_plot = TextField(
        verbose_name="Строения на участке",
        help_text="Введите текст",
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

    village_fences = ForeignKey(
        models.attributes.VillageFences,
        on_delete=RESTRICT,
        null=True,
        blank=True,
        verbose_name="Ограждение поселка",
        help_text="Выберите из списка, или создайте новое '+'",
    )

    object_description = MDTextField(
        null=True,
        blank=True,
        verbose_name="Описание объекта",
        help_text="Текст с форматированием",
    )

    # coordinates = OneToOneField(
    #     models.attributes.Coordinates,
    #     on_delete=RESTRICT,
    #     null=True,
    #     blank=True,
    #     verbose_name="Координаты объекта",
    #     help_text="Широта, Долгота",
    # )

    yandex_map_link = TextField(
        verbose_name="Ссылка на YandexMap",
        help_text="скопируйте ссылку iframe из браузера и вставьте в это поле",
        blank=True,
        null=True,
    )

    date_sale = DateField(
        verbose_name="Дата продажи",
        help_text="введите дату",
        blank=True,
        null=True,
    )

    you_tube_link = TextField(
        verbose_name="Ссылка на YouTube",
        help_text="скопируйте ссылку из браузера и вставьте в это поле",
        blank=True,
        null=True,
    )
    # t

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Объекты недвижимости"
        verbose_name_plural = "Объекты недвижимости"
