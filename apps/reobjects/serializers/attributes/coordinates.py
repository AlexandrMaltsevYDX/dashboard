from rest_framework import serializers
from apps.reobjects import models


class CoordinatesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Coordinates
        fields = "__all__"
