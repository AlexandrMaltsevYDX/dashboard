from rest_framework import viewsets, mixins

from apps.users.models import EmployeeProfileModel, EmployeeProfileAvatarModel
from apps.users.serializers import EmployeeProfileModelSerializer


#
class EmployeeProfileListViewset(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = EmployeeProfileModel.objects.all().prefetch_related("avatars")
    serializer_class = EmployeeProfileModelSerializer
    http_method_names = [
        "put",
        "get",
    ]
