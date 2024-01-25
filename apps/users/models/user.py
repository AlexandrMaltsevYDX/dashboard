from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


from apps.core.models.base import BaseModel


class User(BaseModel, AbstractUser):
    class Meta(AbstractUser.Meta):
        pass


class Group(Group):
    class Meta:
        proxy = True
