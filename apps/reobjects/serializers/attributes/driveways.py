from rest_framework import serializers
from apps.reobjects import models


class DrivewaysModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Driveways
        fields = "__all__"
