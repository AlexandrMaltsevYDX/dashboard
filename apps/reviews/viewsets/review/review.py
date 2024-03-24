from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.core.serializers import StandardResultsSetPagination
from apps.reviews import models, serializers


class ReviewModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.review.Review.objects.all()
    serializer_class = serializers.review.ReviewModelSerializer
    pagination_class = StandardResultsSetPagination
    parser_classes = [
        parsers.FormParser,
    ]

    http_method_names = [
        "post",
        # "delete",
        # "put",
        "get",
    ]
