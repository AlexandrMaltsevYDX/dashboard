from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class RepairModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Repair.objects.all()
    serializer_class = serializers.attributes.RepairModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
