from django.urls import include, path
from apps.blog import routers

urlpatterns = [
    path("", include(routers.posts.router.urls)),
]
