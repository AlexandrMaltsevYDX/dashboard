from rest_framework import serializers
from apps.reobjects import models


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.place.City
        fields = "__all__"
