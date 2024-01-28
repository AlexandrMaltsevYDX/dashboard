from rest_framework import serializers
from apps.reobjects import models


class ReliefAreaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.ReliefArea
        fields = "__all__"
