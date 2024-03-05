from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.core.serializers import StandardResultsSetPagination
from apps.blog import (
    models,
    serializers,
)


class PostImageModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.posts.PostImageModel.objects.all()
    serializer_class = serializers.posts.PostImageModelSerializer
    parser_classes = [
        parsers.MultiPartParser,
    ]

    http_method_names = [
        "post",
        # "delete",
        # "put",
        # "get",
    ]
