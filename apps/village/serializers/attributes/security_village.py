from rest_framework import serializers
from apps.village import models


class SecurityVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.SecurityVillage
        fields = "__all__"
