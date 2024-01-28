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
    queryset = models.place.Coordinates.objects.all()
    serializer_class = serializers.place.CoordinatesModelSerializer
    http_method_names = [
        "post",
        "delete",
        "put",
        "get",
    ]
