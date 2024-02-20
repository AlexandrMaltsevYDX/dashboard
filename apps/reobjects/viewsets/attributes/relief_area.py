from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class ReliefAreaModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.ReliefArea.objects.all()
    serializer_class = serializers.attributes.ReliefAreaModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
