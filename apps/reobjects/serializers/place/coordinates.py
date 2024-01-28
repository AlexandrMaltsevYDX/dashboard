from rest_framework import serializers
from apps.reobjects import models


class CoordinatesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.place.Coordinates
        fields = "__all__"
