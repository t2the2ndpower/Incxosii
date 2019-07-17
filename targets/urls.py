from django.urls import path, include
from . import views

# API related imports
from rest_framework import routers

# API Rouer settings
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'target', views.TargetViewSet)
router.register(r'target_assignments', views.TargetAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]