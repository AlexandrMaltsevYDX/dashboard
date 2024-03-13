from rest_framework import serializers
from apps.reobjects import models


class WCModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.WC
        fields = "__all__"
