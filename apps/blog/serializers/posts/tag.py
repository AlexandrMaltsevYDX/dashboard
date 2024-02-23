from rest_framework import serializers
from apps.blog import models


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["name"]
        model = models.posts.Tag
        fields = ["uuid", "name"]
