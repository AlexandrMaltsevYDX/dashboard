from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class EngineeringServicesModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.EngineeringServices.objects.all()
    serializer_class = serializers.attributes.EngineeringServicesModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
