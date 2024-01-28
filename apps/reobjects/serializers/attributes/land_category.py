from rest_framework import serializers
from apps.reobjects import models


class LandCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.LandCategory
        fields = "__all__"
