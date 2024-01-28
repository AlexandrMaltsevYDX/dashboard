from rest_framework import serializers
from apps.reobjects import models


class FoundationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Foundation
        fields = "__all__"
