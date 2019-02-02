from rest_framework import viewsets, mixins

from social.models import Social
from social.serializers import SocialSerializer


class SocialViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
