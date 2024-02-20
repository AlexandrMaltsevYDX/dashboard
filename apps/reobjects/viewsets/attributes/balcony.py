from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class BalconyModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Balcony.objects.all()
    serializer_class = serializers.attributes.BalconyModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
