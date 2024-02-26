from rest_framework import serializers
from apps.reobjects import models


class VisibleOnSiteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attributes.VisibleOnSite
        fields = "__all__"
