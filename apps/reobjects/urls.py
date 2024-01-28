from django.urls import include, path
from apps.reobjects import routers

urlpatterns = [
    path("place/", include(routers.place.router.urls)),
    path("services/", include(routers.service.router.urls)),
    path("attributes/", include(routers.attributes.router.urls)),
]
