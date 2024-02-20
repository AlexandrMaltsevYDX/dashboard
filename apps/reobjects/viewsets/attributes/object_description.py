from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class ObjectDescriptionModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.ObjectDescription.objects.all()
    serializer_class = serializers.attributes.ObjectDescriptionModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
