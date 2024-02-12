from rest_framework import serializers
from apps.reobjects import models


class ReObjectPlanModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.objects_re.ReObjectPlanModel
        fields = "__all__"
