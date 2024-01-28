from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class TagModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.place.Tag.objects.all()
    serializer_class = serializers.place.TagModelSerializer
    http_method_names = [
        "post",
        "delete",
        "put",
        "get",
    ]
