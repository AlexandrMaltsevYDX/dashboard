from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class WindowsOrientationModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.WindowsOrientation.objects.all()
    serializer_class = serializers.attributes.WindowsOrientationModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
