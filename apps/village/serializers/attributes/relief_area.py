from rest_framework import serializers
from apps.village import models


class ReliefAreaPlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.ReliefAreaPlot
        fields = "__all__"
