from rest_framework import routers
from apps.users.viewsets import UserViewSet, EmployeeProfileListViewset

router = routers.DefaultRouter()

router.register(r"", UserViewSet)
router.register(r"profile", EmployeeProfileListViewset)
