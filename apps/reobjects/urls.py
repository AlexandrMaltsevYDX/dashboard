from django.urls import include, path
from apps.reobjects import routers
from django.urls import re_path
from . import views

urlpatterns = [
    # path("services/", include(routers.service.router.urls)),
    # path("attributes/", include(routers.attributes.router.urls)),
    path("", include(routers.objects_re.router.urls)),
    # ex: /polls/
]

modulepatterns = [
    path("custom/<str:uuid>", views.index, name="index"),
    re_path(
        r"^custom/(?P<model>\w+)/(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})&(?P<imagetype>\w+)$",
        views.sorting,
        name="test",
    ),
    # path("update_values/", views.update_values, name="update_values"),
    re_path(
        r"^update_values/(?P<model>\w+)/(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})&(?P<imagetype>\w+)$",
        views.update_values,
        name="update_values",
    ),
]
