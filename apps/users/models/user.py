from django.contrib.auth.models import AbstractUser

from apps.core.models.base import BaseModel


class User(BaseModel, AbstractUser):
    class Meta(AbstractUser.Meta):
        pass


