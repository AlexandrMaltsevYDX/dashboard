from rest_framework import (
    viewsets,
    mixins,
)

from apps.village import (
    models,
    serializers,
)


class VillageModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.village.Village.objects.all()
    serializer_class = serializers.village.VillageModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
