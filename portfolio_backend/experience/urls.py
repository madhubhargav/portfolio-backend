from rest_framework import routers

from experience.views import ExperienceViewSet, ExperienceDescriptionViewSet


EXPERIENCE_ROUTER = routers.DefaultRouter()
EXPERIENCE_ROUTER.register(r'experience', ExperienceViewSet)

EXPERIENCE_DESCRIPTION_ROUTER = routers.DefaultRouter()
EXPERIENCE_DESCRIPTION_ROUTER.register(r'experience-description', ExperienceDescriptionViewSet)
