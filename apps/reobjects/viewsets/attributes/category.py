from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class CategoryModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.Category.objects.all()
    serializer_class = serializers.attributes.CategoryModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
