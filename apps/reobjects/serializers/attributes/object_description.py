from rest_framework import serializers
from apps.reobjects import models


class ObjectDescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.ObjectDescription
        fields = "__all__"
