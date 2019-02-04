from rest_framework import routers

from project.views import ProjectViewSet, ProjectDescriptionViewSet


PROJECT_ROUTER = routers.DefaultRouter()
PROJECT_ROUTER.register(r'project', ProjectViewSet)

PROJECT_DESCRIPTION_ROUTER = routers.DefaultRouter()
PROJECT_DESCRIPTION_ROUTER.register(r'project-description', ProjectDescriptionViewSet)
