from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class PlaceModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.place.Place.objects.all()
    serializer_class = serializers.place.PlaceModelSerializer
    http_method_names = [
        "post",
        "delete",
        "put",
        "get",
    ]
