from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.reobjects import models, serializers


class ReObjectVisibleOnSiteModelSerializer(ModelSerializer):
    # display_pages = SlugRelatedField(read_only=True, slug_field="value")
    display_pages = serializers.attributes.VisibleOnSiteModelSerializer(
        # many=True,
        read_only=True,
    )

    class Meta:
        model = models.objects_re.ReObjectVisibleOnSite
        fields = [
            "display_pages",
        ]
