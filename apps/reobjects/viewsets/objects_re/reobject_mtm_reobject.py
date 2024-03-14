from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.core.serializers import StandardResultsSetPagination
from apps.reobjects import (
    models,
    serializers,
)


class ReObjectCloseModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.objects_re.ReObjectClose.objects.all()
    serializer_class = serializers.objects_re.ReObjectCloseModelSerializer
    filterset_fields = [
        "re_object__uuid",
    ]
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
