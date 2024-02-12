from rest_framework import serializers
from apps.reobjects import models


class WindowMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.WindowMaterial
        fields = "__all__"
