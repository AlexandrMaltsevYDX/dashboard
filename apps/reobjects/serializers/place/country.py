from rest_framework import serializers
from apps.reobjects import models


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.place.Country
        fields = "__all__"
