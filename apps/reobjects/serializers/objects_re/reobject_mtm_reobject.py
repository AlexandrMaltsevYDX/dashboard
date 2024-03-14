from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
    StringRelatedField,
)
from apps.reobjects import models, serializers


class ReObjectCloseModelSerializer(ModelSerializer):
    # display_pages = SlugRelatedField(read_only=True, slug_field="value")
    re_object = SlugRelatedField(
        # many=True,
        read_only=True,
        slug_field="uuid",
    )
    close_re_object = SlugRelatedField(
        # many=True,
        read_only=True,
        slug_field="uuid",
    )

    class Meta:
        model = models.objects_re.ReObjectClose
        fields = [
            "re_object",
            "close_re_object",
        ]
