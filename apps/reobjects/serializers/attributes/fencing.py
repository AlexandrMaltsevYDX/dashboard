from rest_framework import serializers
from apps.reobjects import models


class FencingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Fencing
        fields = "__all__"
