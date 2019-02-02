from rest_framework import routers

from person.views import PersonViewSet


PERSON_ROUTER = routers.DefaultRouter()
PERSON_ROUTER.register(r'person', PersonViewSet)
