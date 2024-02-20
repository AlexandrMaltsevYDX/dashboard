from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class SalesMethodModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.SalesMethod.objects.all()
    serializer_class = serializers.attributes.SalesMethodModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
