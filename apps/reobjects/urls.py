from django.urls import include, path
from apps.reobjects import routers
from . import views

urlpatterns = [
    # path("services/", include(routers.service.router.urls)),
    # path("attributes/", include(routers.attributes.router.urls)),
    path("", include(routers.objects_re.router.urls)),
    # ex: /polls/
]

modulepatterns = [
    path("custom/<str:uuid>", views.index, name="index"),
    path("update_values/", views.update_values, name="update_values"),
]
