from rest_framework import serializers
from apps.reobjects import models


class DistrictModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.place.District
        fields = "__all__"
