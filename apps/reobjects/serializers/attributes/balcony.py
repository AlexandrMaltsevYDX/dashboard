from rest_framework import serializers
from apps.reobjects import models


class BalconyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Balcony
        fields = "__all__"
