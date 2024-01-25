from rest_framework import routers
from apps.users.viewsets import UserViewSet, EmployeeProfileListViewset

router = routers.DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"profile", EmployeeProfileListViewset)
