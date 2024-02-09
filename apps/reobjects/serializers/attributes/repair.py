from rest_framework import serializers
from apps.reobjects import models


class RepairModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Repair
        fields = "__all__"
