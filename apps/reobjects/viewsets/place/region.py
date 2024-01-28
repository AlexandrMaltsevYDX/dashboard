from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class RegionModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.place.Region.objects.all()
    serializer_class = serializers.place.RegionModelSerializer
    http_method_names = [
        "post",
        "delete",
        "put",
        "get",
    ]
