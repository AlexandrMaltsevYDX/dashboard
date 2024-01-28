from rest_framework import serializers
from apps.reobjects import models


class WallMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.WallMaterial
        fields = "__all__"
