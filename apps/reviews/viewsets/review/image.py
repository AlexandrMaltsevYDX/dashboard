from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.core.serializers import StandardResultsSetPagination
from apps.reviews import (
    models,
    serializers,
)


class ReviewImageModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.review.ReviewImageModel.objects.all()
    serializer_class = serializers.review.ReviewImageSerializers
    parser_classes = [
        parsers.MultiPartParser,
    ]

    http_method_names = [
        "post",
        # "delete",
        # "put",
        # "get",
    ]
