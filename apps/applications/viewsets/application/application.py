from rest_framework import (
    viewsets,
    mixins,
    parsers,
)

from apps.applications import (
    models,
    serializers,
    tasks,
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

    def perform_create(self, serializer):
        super().perform_create(serializer)
        tasks.send_email.delay(
            subject="Заявка",
            message=f"""
            {serializer.data['text'] }
            {serializer.data['applicant'] }
            {serializer.data['contact'] }
            """,
            recipient="AlexandrMaltsve@yandex.ru",
        )
