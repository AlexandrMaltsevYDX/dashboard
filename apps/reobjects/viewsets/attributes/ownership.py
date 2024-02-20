from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class OwnershipModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Ownership.objects.all()
    serializer_class = serializers.attributes.OwnershipModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
