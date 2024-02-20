from rest_framework import (
    viewsets,
    mixins,
    filters,
)

from apps.core.serializers import StandardResultsSetPagination
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
    pagination_class = StandardResultsSetPagination
    filterset_fields = [
        "visible_on_site",
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
        "category__name",
        "place",
        "metro",
        "land_category__value",
        "approve_usage__value",
        "ownership__value",
        "repair__name",
        "balcony__name",
        "sales_method__name",
        "type_house__name",
        "foundation__value",
        "wall_material__value",
        "object_description",
    ]
    http_method_names = [
        # "post",
        # "delete",
        # "put",
        "get",
    ]
