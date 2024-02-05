from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)
from apps.reobjects import models, serializers
from .image import ReObjectImageModelSerializer
from .reobject_mtm_enjineeringservice import ReObjectEngineeringServicesModelSerializer


class ReObjectModelSerializer(ModelSerializer):
    # category = serializers.attributes.CategoryModelSerializer()
    # type_house = serializers.attributes.TypeHouseModelSerializer()
    # windows_orientation = serializers.attributes.WindowsOrientationModelSerializer()
    # ownership = serializers.attributes.OwnershipModelSerializer()
    # land_category = serializers.attributes.LandCategoryModelSerializer()
    # relief_area = serializers.attributes.ReliefAreaModelSerializer()
    # fencing = serializers.attributes.FencingModelSerializer()
    # foundation = serializers.attributes.FoundationModelSerializer()
    # wall_material = serializers.attributes.WallMaterialModelSerializer()
    # village_fences = serializers.attributes.VillageFencesModelSerializer()
    # object_description = serializers.attributes.ObjectDescriptionModelSerializer()

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
    object_description = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="value",
    )
    photos = ReObjectImageModelSerializer(
        many=True,
        read_only=True,
    )
    images = ListField(child=FileField(required=False), write_only=True)
    services = ReObjectEngineeringServicesModelSerializer(
        many=True,
        read_only=True,
        source="re_objects",
    )

    class Meta:
        model = models.objects_re.ReObject
        fields = [
            "id",
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
            "land_area",
            "relief_area",
            "fencing",
            "foundation",
            "wall_material",
            "buildings_on_site",
            "buildings_of_villages",
            "village_fences",
            "object_description",
            "photos",
            "images",
            "services",
        ]
