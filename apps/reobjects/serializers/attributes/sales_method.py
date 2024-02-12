from rest_framework import serializers
from apps.reobjects import models


class SalesMethodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.SalesMethod
        fields = "__all__"
