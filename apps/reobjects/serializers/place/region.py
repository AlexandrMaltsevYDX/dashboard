from rest_framework import serializers
from apps.reobjects import models


class RegionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.place.Region
        fields = "__all__"
