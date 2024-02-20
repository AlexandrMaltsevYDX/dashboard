from rest_framework import (
    viewsets,
    mixins,
)

from apps.blog import (
    models,
    serializers,
)
from apps.core.serializers import StandardResultsSetPagination


class PostModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.posts.Post.objects.all()
    serializer_class = serializers.posts.PostModelSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = [
        "author__username",
    ]
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
