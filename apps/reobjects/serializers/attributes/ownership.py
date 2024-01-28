from rest_framework import serializers
from apps.reobjects import models


class OwnershipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Ownership
        fields = "__all__"
