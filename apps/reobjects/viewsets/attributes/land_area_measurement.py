from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class AreaOfMeasurementModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.AreaOfMeasurement.objects.all()
    serializer_class = serializers.attributes.AreaOfMeasurementModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
