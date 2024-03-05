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


class ReObjectImageModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.objects_re.ReObjectImage.objects.all()
    serializer_class = serializers.objects_re.ReObjectImageModelSerializer
    parser_classes = [
        parsers.MultiPartParser,
    ]

    http_method_names = [
        "post",
        # "delete",
        # "put",
        # "get",
    ]
