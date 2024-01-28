from rest_framework import serializers
from apps.reobjects import models


class VillageFencesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.VillageFences
        fields = "__all__"
