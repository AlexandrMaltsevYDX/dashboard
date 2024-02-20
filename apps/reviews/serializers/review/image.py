from apps.reviews import models, serializers
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    ListField,
    FileField,
    SlugRelatedField,
    CharField,
    PrimaryKeyRelatedField,
)


class ReviewImageSerializers(ModelSerializer):
    class Meta:
        model = models.review.ReviewImageModel
        fields = "__all__"

    # def create(self, validated_data):
    #     review = models.review.Review.objects.get(uuid=self.review)
    #     images = validated_data.pop("images")
    #     for img in images:
    #         photo = models.review.ReviewImageModel.objects.create(
    #             image=img, review=review, **validated_data
    #         )
    #     return images
    #
    # # def save(self, *args, **kwargs):
    # #     print("===========>     validated_data", self.validated_data)
    # #     images_data = self.validated_data.pop("images")
    # #     # super().save(*args, **kwargs)
    # #     if images_data:
    # #         print("===========>     попали")
    # #         for image in images_data:
    # #             models.review.ReviewImageModel.objects.create(
    # #                 review=self.validated_data["review"], image=image
    # #             )
    # #     return self.instance
