from rest_framework import (
    viewsets,
    mixins,
)

from apps.reobjects import (
    models,
    serializers,
)


class VillageFencesModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.attributes.VillageFences.objects.all()
    serializer_class = serializers.attributes.VillageFencesModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
