from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
)
from apps.village import models, serializers
from ..relationships import (
    VillageEngineeringServicesModelSerializer,
    VillageEmployeeModelSerializer,
)
from .image import VillageImageModelSerializer
from .plan_image import VillagePlanModelSerializer


class VillageModelSerializer(ModelSerializer):
    wall_material = SlugRelatedField(
        slug_field="value",
        read_only=True,
    )

    foundation = SlugRelatedField(
        slug_field="value",
        read_only=True,
    )

    area_of_plot_measurement = SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    category_land = SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    relief_area_plot = SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    fencing_village = SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    security_village = SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    photo_images = VillageImageModelSerializer(
        many=True,
        read_only=True,
        source="villageimages",
    )
    plans_images = VillagePlanModelSerializer(
        many=True,
        read_only=True,
        source="villageplans",
    )
    # services
    display_engineering_services = VillageEngineeringServicesModelSerializer(
        many=True,
        read_only=True,
        source="villages",
    )

    # agents
    display_agents = VillageEmployeeModelSerializer(
        many=True,
        read_only=True,
        source="villageemployees",
    )

    class Meta:
        model = models.village.Village
        fields = [
            "uuid",
            "id",
            # "visible_on_site",
            "name",
            "distance_CAD",
            "area_of_houses",
            "wall_material",
            "buildings_of_villages",
            "foundation",
            "area_of_plot_measurement",
            "category_land",
            "relief_area_plot",
            "area_of_plot",
            "relief_area_plot",
            "display_engineering_services",
            "photo_images",
            "plans_images",
            "display_agents",
            "fencing_village",
            "security_village",
            "object_description",
            "buildings_on_plot",
            "yandex_map_link",
            "you_tube_link",
            "price",
            "place",
            "infra",
        ]


#
# class Village(TimeStampedModel, BaseModel):
#     id = IntegerField(
#         blank=True,
#         null=True,
#         verbose_name="ID посёлка",
#     )
#
#     visible_on_site = BooleanField(
#         blank=True,
#         null=True,
#         verbose_name="Отображать на сайте",
#     )
#
#     name = TextField(
#         verbose_name="Название объекта",
#         help_text="Адрес",
#         blank=True,
#         null=True,
#     )
#
#     distance_CAD = FloatField(
#         null=True,
#         blank=True,
#         verbose_name="Расстояние до кад",
#         help_text="введите знaчение в КМ, например '1.2' ",
#     )
#     area_of_houses = TextField(
#         null=True,
#         blank=True,
#         verbose_name="Площадь домов в кв.м",
#         help_text="введите знaчение, например '100 - 200' ",
#     )
#
#     wall_material = ForeignKey(
#         house_attributes.WallMaterial,
#         on_delete=RESTRICT,
#         null=True,
#         blank=True,
#         verbose_name="Материал стен домов в поселке",
#         help_text="Выберете значение из списка, или создайте новое '+'",
#     )
#
#     buildings_of_villages = PositiveIntegerField(
#         verbose_name="Количество домов в поселке",
#         help_text="Количество домов в поселке",
#         null=True,
#         blank=True,
#     )
#
#     foundation = ForeignKey(
#         house_attributes.Foundation,
#         on_delete=RESTRICT,
#         null=True,
#         blank=True,
#         verbose_name="Фундамент домов",
#         help_text="Выберете значение из списка, или создайте новое '+'",
#     )
#
#     area_of_plot = FloatField(
#         null=True,
#         blank=True,
#         verbose_name="Площадь одного участка",
#         help_text="введите знaчение, например '1.2' ",
#     )
#
#     area_of_plot_measurement = ForeignKey(
#         attributes.AreaOfPlotMeasurement,
#         on_delete=RESTRICT,
#         null=True,
#         blank=True,
#         verbose_name="Единица измерения площади одного участка",
#         help_text="Выберете значение из списка, или создайте новое '+'",
#     )
#
#     category_land = ForeignKey(
#         attributes.CategoryLandPlot,
#         on_delete=RESTRICT,
#         null=True,
#         blank=True,
#         verbose_name="Категория земель участков",
#         help_text="Выберете значение из списка, или создайте новое '+'",
#     )
#
#     relief_area_plot = ForeignKey(
#         attributes.ReliefAreaPlot,
#         on_delete=RESTRICT,
#         null=True,
#         blank=True,
#         verbose_name="Рельеф участков",
#         help_text="Выберете значение из списка, или создайте новое '+'",
#     )
#
#     fencing_village = ForeignKey(
#         attributes.FencingVillage,
#         on_delete=RESTRICT,
#         null=True,
#         blank=True,
#         verbose_name="Ограждение поселка",
#         help_text="Выберете значение из списка, или создайте новое '+'",
#     )
#
#     security_village = ForeignKey(
#         attributes.SecurityVillage,
#         on_delete=RESTRICT,
#         null=True,
#         blank=True,
#         verbose_name="Охрана поселка",
#         help_text="Выберете значение из списка, или создайте новое '+'",
#     )
#
#     object_description = MDTextField(
#         null=True,
#         blank=True,
#         verbose_name="Описание объекта",
#         help_text="Текст с форматированием",
#     )
#
#     buildings_on_plot = TextField(
#         verbose_name="Строения на участке",
#         help_text="Опишите строения на участке",
#         blank=True,
#         null=True,
#     )
#
#     you_tube_link = TextField(
#         verbose_name="Ссылка на YouTube",
#         help_text="скопируйте ссылку из браузера и вставьте в это поле",
#         blank=True,
#         null=True,
#     )
#
#     yandex_map_link = TextField(
#         verbose_name="Ссылка на YandexMap",
#         help_text="скопируйте ссылку iframe из браузера и вставьте в это поле",
#         blank=True,
#         null=True,
#     )
