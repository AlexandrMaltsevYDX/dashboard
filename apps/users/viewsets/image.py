from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.core.serializers import StandardResultsSetPagination
from apps.users import (
    models,
    serializers,
)


class EmployeeProfileAvatarModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.image.EmployeeProfileAvatarModel.objects.all()
    serializer_class = serializers.profile.EmployeeProfileAvatarModelSerializer
    parser_classes = [
        parsers.MultiPartParser,
    ]

    http_method_names = [
        "post",
        # "delete",
        # "put",
        # "get",
    ]
