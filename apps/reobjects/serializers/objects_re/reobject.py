from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)
from apps.reobjects import models, serializers
from .image import ReObjectImageModelSerializer
from .plan_image import ReObjectPlanModelSerializer
from .reobject_mtm_enjineeringservice import ReObjectEngineeringServicesModelSerializer
from .reobject_mtm_employee import ReObjectEmployeeModelSerializer
from .reobject_mtm_visibleonsite import ReObjectVisibleOnSiteModelSerializer
from .reobject_mtm_reobject import ReObjectCloseModelSerializer


class ReObjectModelSerializer(ModelSerializer):
    category = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    land_category = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    approve_usage = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    ownership = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    land_area_measurement = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    window_material = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    windows_orientation = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    repair = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    balcony = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    sales_method = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    type_house = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    lift = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    foundation = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    wall_material = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    relief_area = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    fencing = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    driveways = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    village_fences = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    # coordinates = serializers.attributes.CoordinatesModelSerializer(
    #     many=False,
    #     read_only=True,
    # )

    # photos
    photo_images = ReObjectImageModelSerializer(
        many=True,
        read_only=True,
    )
    photo_images_files = ListField(
        child=FileField(required=False),
        write_only=True,
    )

    # plans
    plans_images = ReObjectPlanModelSerializer(
        many=True,
        read_only=True,
    )

    plans_images_files = ListField(
        child=FileField(required=False),
        write_only=True,
    )

    # services
    display_engineering_services = ReObjectEngineeringServicesModelSerializer(
        many=True,
        read_only=True,
        source="re_objects",
    )

    # agents
    display_agents = ReObjectEmployeeModelSerializer(
        many=True,
        read_only=True,
        source="reobjectemployees",
    )

    display_pages = ReObjectVisibleOnSiteModelSerializer(
        many=True,
        read_only=True,
        source="reobjectsite",
    )

    wc = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    class Meta:
        model = models.objects_re.ReObject
        fields = [
            "uuid",
            "created_at",
            "id",
            "name",
            "category",
            "place",
            "distance_CAD",
            "metro",
            "land_category",
            "approve_usage",
            "ownership",
            "area_house",
            "land_area_measurement",
            "area_plot",
            "area_flat",
            "living_area",
            "kitchen_area",
            "area_room",
            "number_of_rooms",
            "number_of_storeys",
            "floor",
            "window_material",
            "windows_orientation",
            "ceiling_height",
            "repair",
            "wc",
            "balcony",
            "sales_method",
            "type_house",
            "date_foundation",
            "lift",
            "foundation",
            "wall_material",
            "price",
            "relief_area",
            "fencing",
            "buildings_on_plot",
            "driveways",
            "village_fences",
            "object_description",
            # "coordinates",
            "yandex_map_link",
            "date_sale",
            "you_tube_link",
            "display_engineering_services",
            "display_agents",
            "plans_images",
            "plans_images_files",
            "photo_images",
            "photo_images_files",
            "display_pages",
            "wc",
        ]


class ReObjectShortModelSerializer(ModelSerializer):
    class Meta:
        model = models.objects_re.ReObject
        fields = [
            "uuid",
        ]
