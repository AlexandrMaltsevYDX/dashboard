from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class WallMaterialModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.WallMaterial.objects.all()
    serializer_class = serializers.attributes.WallMaterialModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
