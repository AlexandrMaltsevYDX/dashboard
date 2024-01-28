from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class CountryModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.place.Country.objects.all()
    serializer_class = serializers.place.CountryModelSerializer
    http_method_names = [
        "post",
        "delete",
        "put",
        "get",
    ]
