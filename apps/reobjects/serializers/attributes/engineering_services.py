from rest_framework import serializers
from apps.reobjects import models


class EngineeringServicesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.EngineeringServices
        fields = "__all__"
