from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.applications import (
    models,
    serializers,
)
from apps.core.serializers import StandardResultsSetPagination


class ApplicationModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.application.Application.objects.all()
    serializer_class = serializers.application.AnnotationModelSerializer
    pagination_class = StandardResultsSetPagination
    parser_classes = [
        parsers.MultiPartParser,
    ]

    http_method_names = [
        "post",
        # "delete",
        # "put",
        "get",
    ]

    # def create(self, request, *args, **kwargs):
    #     print("===========>     create", request.data)
    #     return super().create(request, *args, **kwargs)
    #
    # def perform_create(self, serializer):
    #     print("===========>     perform_create")
    #     super().perform_create(serializer)
