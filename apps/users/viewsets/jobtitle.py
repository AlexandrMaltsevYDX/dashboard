from rest_framework import (
    viewsets,
    mixins,
)

from apps.users import (
    models,
    serializers,
)


class JobTitleModelViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.jobtitle.JobTitle.objects.all()
    serializer_class = serializers.jobtitle.JobTitleModelSerializer
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
