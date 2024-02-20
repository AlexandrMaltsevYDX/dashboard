from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class LandCategoryModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.LandCategory.objects.all()
    serializer_class = serializers.attributes.LandCategoryModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
