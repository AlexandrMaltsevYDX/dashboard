from rest_framework import viewsets, mixins

from apps.core.serializers import StandardResultsSetPagination
from apps.users.models import EmployeeProfileModel, EmployeeProfileAvatarModel
from apps.users.serializers import EmployeeProfileModelSerializer


class EmployeeProfileViewset(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = EmployeeProfileModel.objects.all()
    serializer_class = EmployeeProfileModelSerializer
    pagination_class = StandardResultsSetPagination
    http_method_names = [
        # "put",
        "get",
    ]
