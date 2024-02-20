from rest_framework import serializers
from apps.reobjects import models


class ApproveUsageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.ApproveUsage
        fields = "__all__"
