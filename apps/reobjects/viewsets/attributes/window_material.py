from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class WindowMaterialModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.WindowMaterial.objects.all()
    serializer_class = serializers.attributes.WindowMaterialModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
