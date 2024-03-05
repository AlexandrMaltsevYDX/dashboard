from rest_framework.routers import DefaultRouter
from apps.blog import viewsets


router = DefaultRouter()

router.register(
    prefix=r"post",
    viewset=viewsets.posts.PostModelViewSet,
)


router.register(
    prefix=r"posts_images",
    viewset=viewsets.posts.PostImageModelViewSet,
)
