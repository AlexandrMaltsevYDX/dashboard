from rest_framework import serializers
from apps.reobjects import models


class StreetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.place.Street
        fields = "__all__"
