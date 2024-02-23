from rest_framework import serializers
from apps.village import models


class AreaOfPlotMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.AreaOfPlotMeasurement
        fields = "__all__"
