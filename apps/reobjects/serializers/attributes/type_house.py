from rest_framework import serializers
from apps.reobjects import models


class TypeHouseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.TypeHouse
        fields = "__all__"
