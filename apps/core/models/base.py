import uuid

from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class BaseImageModel(BaseModel):
    # todo
    # @staticmethod
    # def get_image_path() -> str:
    #     return f'images/'

    image = models.FileField(upload_to="images/")

    class Meta:
        abstract = True
