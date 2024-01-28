from rest_framework import serializers
from apps.reobjects import models


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.place.Tag
        fields = "__all__"
