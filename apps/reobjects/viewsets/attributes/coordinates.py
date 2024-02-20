from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class CoordinatesModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Coordinates.objects.all()
    serializer_class = serializers.attributes.CoordinatesModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
