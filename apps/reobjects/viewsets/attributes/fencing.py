from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class FencingModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Fencing.objects.all()
    serializer_class = serializers.attributes.FencingModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
