from django.db import models

from apps.core.models.base import BaseModel, BaseImageModel
from apps.users.models.profile import UserProfileModel
from src import settings


class UserAvatarModel(BaseImageModel):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)


