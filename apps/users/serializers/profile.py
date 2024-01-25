from rest_framework import serializers
from apps.users.models import EmployeeProfileModel, EmployeeProfileAvatarModel


class EmployeeProfileAvatarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfileAvatarModel
        fields = ["uuid", "profile", "image"]


class EmployeeProfileModelSerializer(serializers.ModelSerializer):
    # images = serializers.ListField(
    #     child=serializers.FileField(required=False), write_only=True
    # )
    avatars = EmployeeProfileAvatarModelSerializer(many=True, read_only=True)

    class Meta:
        model = EmployeeProfileModel
        fields = ["uuid", "avatars"]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        employee_profile = EmployeeProfileModel.objects.create(**validated_data)

        for image_data in images_data:
            EmployeeProfileAvatarModel.objects.create(
                profile=employee_profile, image=image_data
            )

        return employee_profile

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])
        instance.profile.uuid = validated_data.get(
            "profile_uuid", instance.profile.uuid
        )
        instance.profile.save()

        for image_data in images_data:
            EmployeeProfileAvatarModel.objects.create(
                profile=instance.profile, image=image_data
            )

        return instance
