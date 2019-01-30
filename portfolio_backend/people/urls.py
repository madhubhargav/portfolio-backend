from rest_framework import routers

from people.views import PeopleViewSet


PEOPLE_ROUTER = routers.DefaultRouter()
PEOPLE_ROUTER.register(r'people', PeopleViewSet, 'people')
