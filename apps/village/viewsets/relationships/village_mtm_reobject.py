from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.core.serializers import StandardResultsSetPagination
from apps.village import (
    models,
    serializers,
)


class ReObjectInVillagesModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.relationships.ReObjectInVillages.objects.all()
    serializer_class = serializers.relationships.ReObjectInVillagesModelSerializer
    filterset_fields = [
        "village__uuid",
    ]
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]


# ReObjectInVillages
