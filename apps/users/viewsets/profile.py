from rest_framework import viewsets, mixins

from apps.users.models import EmployeeProfileModel, EmployeeProfileAvatarModel
from apps.users.serializers import EmployeeProfileModelSerializer


#
class EmployeeProfileListViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = EmployeeProfileModel.objects.all().prefetch_related("avatars")
    serializer_class = EmployeeProfileModelSerializer
