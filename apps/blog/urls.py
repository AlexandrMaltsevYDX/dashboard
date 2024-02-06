from django.urls import include, path
from apps.blog import routers

urlpatterns = [
    path("blog/", include(routers.posts.router.urls)),
]
