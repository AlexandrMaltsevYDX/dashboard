from rest_framework import serializers
from apps.reobjects import models


class ReObjectImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.objects_re.ReObjectImage
        fields = "__all__"
