from rest_framework import serializers
from apps.village import models


class VillageImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.village.VillageImageModel
        fields = "__all__"
