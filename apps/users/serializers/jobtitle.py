from rest_framework import serializers
from apps.users.models import JobTitle


class JobTitleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = "__all__"
