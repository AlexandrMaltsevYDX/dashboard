from rest_framework import routers
from apps.users.viewsets import (
    UserViewSet,
    EmployeeProfileViewset,
    EmployeeProfileAvatarModelViewSet,
    JobTitleModelViewSet,
)

profile_images_router = routers.DefaultRouter()

# router.register(r"", UserViewSet)
# router.register(r"job_title", JobTitleModelViewSet)
profile_images_router.register(r"profiles_images", EmployeeProfileAvatarModelViewSet)
