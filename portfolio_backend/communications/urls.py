from rest_framework import routers

from communications.views import CommunicationsViewSet


COMMUNICATIONS_ROUTER = routers.DefaultRouter()
COMMUNICATIONS_ROUTER.register(r'communications', CommunicationsViewSet, 'communications')
