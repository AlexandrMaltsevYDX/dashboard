from rest_framework import serializers
from apps.village import models


class FencingVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.FencingVillage
        fields = "__all__"
