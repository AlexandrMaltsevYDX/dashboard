from django.db import models

from apps.core.models.base import BaseModel
from src import settings


class ContactModel(BaseModel):
    """
    telegram, instagram, email, phone number
    """
    name = models.CharField(max_length=250, blank=True)


class UserContactModel(BaseModel):
    # todo зависимость от name, validators и т д
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.ForeignKey(ContactModel, on_delete=models.CASCADE)
    value = models.CharField(max_length=250, blank=True)
