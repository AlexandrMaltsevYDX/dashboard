from rest_framework import serializers
from apps.blog import models


class PostImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.posts.PostImageModel
        fields = "__all__"
