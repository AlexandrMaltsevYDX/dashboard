from rest_framework import serializers
from apps.village import models


class CategoryLandPlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.CategoryLandPlot
        fields = "__all__"
