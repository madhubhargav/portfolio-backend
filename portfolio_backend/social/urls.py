from rest_framework import routers

from social.views import SocialViewSet


SOCIAL_ROUTER = routers.DefaultRouter()
SOCIAL_ROUTER.register(r'social', SocialViewSet)
