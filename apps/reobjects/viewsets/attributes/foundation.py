from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class FoundationModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Foundation.objects.all()
    serializer_class = serializers.attributes.FoundationModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
