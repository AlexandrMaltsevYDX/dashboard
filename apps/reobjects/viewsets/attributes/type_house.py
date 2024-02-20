from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class TypeHouseModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.TypeHouse.objects.all()
    serializer_class = serializers.attributes.TypeHouseModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
