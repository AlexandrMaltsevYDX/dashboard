from apps.reviews import models, serializers
from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    FileField,
    SlugRelatedField,
)
from .image import ReviewImageSerializers
from apps.reviews import models


class ReviewModelSerializer(ModelSerializer):
    photos = ReviewImageSerializers(
        source="reviewimages",
        many=True,
        read_only=True,
    )
    # images = ListField(
    #     child=FileField(
    #         required=False,
    #     ),
    #     write_only=True,
    #     required=False,
    # )

    class Meta:
        model = models.review.Review
        fields = [
            "uuid",
            "text",
            "author_name",
            "date_sale",
            # "images",
            "photos",
            "link_to_src",
        ]

    # def save(self, *args, **kwargs):
    #     print("===========>     validated_data", self.validated_data)
    #     images_data = self.validated_data.pop("images")
    #     super().save(*args, **kwargs)
    #     if images_data:
    #         self.instance.reviewimages.all().delete()
    #         for image in images_data:
    #             self.instance.reviewimages.create(image=image)
    #     return self.instance
