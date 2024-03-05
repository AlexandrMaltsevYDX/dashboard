from django.urls import include, path
from apps.reobjects import routers

urlpatterns = [
    # path("services/", include(routers.service.router.urls)),
    # path("attributes/", include(routers.attributes.router.urls)),
    path("", include(routers.objects_re.router.urls)),
]
