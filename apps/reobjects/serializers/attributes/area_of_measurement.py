from rest_framework import serializers
from apps.reobjects import models


class AreaOfMeasurementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.AreaOfMeasurement
        fields = "__all__"
