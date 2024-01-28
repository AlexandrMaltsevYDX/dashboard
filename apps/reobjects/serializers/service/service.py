from rest_framework import serializers
from apps.reobjects import models


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.service.Service
        fields = "__all__"
