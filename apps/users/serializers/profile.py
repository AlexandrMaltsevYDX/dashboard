from rest_framework import serializers
from apps.users.models import EmployeeProfileModel, EmployeeProfileAvatarModel
from .jobtitle import JobTitleModelSerializer


class EmployeeProfileAvatarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfileAvatarModel
        fields = ["uuid", "objectModel", "image"]


class EmployeeProfileModelSerializer(serializers.ModelSerializer):
    # images = serializers.ListField(
    #     child=serializers.FileField(required=False), write_only=True
    # )
    avatars = EmployeeProfileAvatarModelSerializer(many=True, read_only=True)
    job_title = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    class Meta:
        model = EmployeeProfileModel
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "location",
            "work_email",
            "phone_number",
            "telegram_link",
            "whatsapp_link",
            "description",
            "job_title",
            "avatars",
            # "images",
        ]

    # def update(self, instance, validated_data):
    #     images_data = validated_data.pop("images")
    #     print("images_data", images_data)
    #     instance.uuid = validated_data.get("uuid")
    #     instance.save()
    #
    #     for avatar in images_data:
    #         EmployeeProfileAvatarModel.objects.create(profile=instance, image=avatar)
    #
    #     return instance
