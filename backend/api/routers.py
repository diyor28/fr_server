from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from api.viewsets import (ClientModelViewSet, VectorsModelViewSet, TasksModelViewSet, LogsViewSet, UsersViewSet)


class NestedRouter(NestedRouterMixin, routers.DefaultRouter):
	pass


router = NestedRouter()

router.register(r'users', UsersViewSet, base_name='users')
router.register(r'clients', ClientModelViewSet, basename='clients')
router.register(r'vectors', VectorsModelViewSet, basename='vectors')

router.register(r'tasks', TasksModelViewSet, base_name='tasks')
router.register(r'logs', LogsViewSet, base_name='logs')
