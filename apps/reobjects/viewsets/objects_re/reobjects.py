from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class ReObjectModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.objects_re.ReObject.objects.all()
    serializer_class = serializers.objects_re.ReObjectModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
