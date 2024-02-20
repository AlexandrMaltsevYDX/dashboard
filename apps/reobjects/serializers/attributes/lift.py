from rest_framework import serializers
from apps.reobjects import models


class LiftModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Lift
        fields = "__all__"
