from rest_framework import serializers
from apps.village import models


class VillagePlanModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.village.VillagePlanModel
        fields = "__all__"
