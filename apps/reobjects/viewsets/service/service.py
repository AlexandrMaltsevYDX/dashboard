from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class ServiceModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.service.Service.objects.all()
    serializer_class = serializers.service.ServiceModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
