from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.FileField(required=False))

    # parsers.FileUploadParser
    class Meta:
        model = User
        fields = ["uuid", "username", "images"]
