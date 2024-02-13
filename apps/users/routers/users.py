from rest_framework import routers
from apps.users.viewsets import (
    UserViewSet,
    EmployeeProfileListViewset,
    JobTitleModelViewSet,
)

router = routers.DefaultRouter()

router.register(r"", UserViewSet)
router.register(r"profile/job_title", JobTitleModelViewSet)
router.register(r"profile", EmployeeProfileListViewset)
