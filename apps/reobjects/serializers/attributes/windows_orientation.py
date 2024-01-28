from rest_framework import serializers
from apps.reobjects import models


class WindowsOrientationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.WindowsOrientation
        fields = "__all__"
