from django.db import models

from apps.core.models.base import BaseModel
from src import settings


class UserProfileModel(BaseModel):
    user = models.OneToOneRel(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
