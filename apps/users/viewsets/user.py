from rest_framework import viewsets, mixins

from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
