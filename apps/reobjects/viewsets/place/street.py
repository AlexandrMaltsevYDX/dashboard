from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class StreetModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.place.Street.objects.all()
    serializer_class = serializers.place.StreetModelSerializer
    http_method_names = [
        "post",
        "delete",
        "put",
        "get",
    ]
