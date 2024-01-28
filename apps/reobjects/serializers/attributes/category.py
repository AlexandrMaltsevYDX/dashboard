from rest_framework import serializers
from apps.reobjects import models


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.Category
        fields = "__all__"
