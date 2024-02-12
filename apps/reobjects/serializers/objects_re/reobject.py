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


class ReObjectModelSerializer(ModelSerializer):
    category = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    type_house = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    repair = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    windows_orientation = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )
    ownership = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )
    land_category = SlugRelatedField(
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
    village_fences = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )

    coordinates = serializers.attributes.CoordinatesModelSerializer(
        many=False,
        read_only=True,
    )
    balcony = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )

    driveways = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
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

    sales_method = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name",
    )
    # photos
    photos = ReObjectImageModelSerializer(
        many=True,
        read_only=True,
    )
    photos_images = ListField(
        child=FileField(required=False),
        write_only=True,
    )

    # plans
    plans = ReObjectPlanModelSerializer(
        many=True,
        read_only=True,
    )

    plans_images = ListField(
        child=FileField(required=False),
        write_only=True,
    )

    # services
    services = ReObjectEngineeringServicesModelSerializer(
        many=True,
        read_only=True,
        source="re_objects",
    )

    class Meta:
        model = models.objects_re.ReObject
        fields = [
            "id",
            "name",
            "category",
            "type_house",
            "number_of_storeys",
            "floor",
            "number_of_rooms",
            "total_area",
            "living_area",
            "kitchen_area",
            "windows_orientation",
            "ownership",
            "land_category",
            "land_area_measurement",
            "land_area",
            "relief_area",
            "fencing",
            "foundation",
            "wall_material",
            "village_fences",
            "object_description",
            "services",
            "coordinates",
            "repair",
            "balcony",
            "driveways",
            "photos",
            "photos_images",
            "plans",
            "plans_images",
            "window_material",
            "sales_method",
        ]
