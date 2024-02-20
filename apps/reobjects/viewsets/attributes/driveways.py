from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class DrivewaysModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Driveways.objects.all()
    serializer_class = serializers.attributes.DrivewaysModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
