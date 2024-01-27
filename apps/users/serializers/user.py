from rest_framework import serializers
from apps.users.models import User, EmployeeProfileModel


class UserSerializer(serializers.ModelSerializer):
    # parsers.FileUploadParser
    class Meta:
        model = User
        fields = ["uuid", "username"]
