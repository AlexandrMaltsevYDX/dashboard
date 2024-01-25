from rest_framework import serializers

from apps.users.models import ReObjectModel, ReObjectImageModel


class ReObjectImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReObjectImageModel
        fields = "__all__"


class ReObjectModelSerializer(serializers.ModelSerializer):
    images_info = ReObjectImageModelSerializer(
        many=True,
        read_only=True,
        source="reobject_images",
    )

    class Meta:
        model = ReObjectModel
        fields = ["name", "images_info"]
