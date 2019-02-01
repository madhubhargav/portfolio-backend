from rest_framework import viewsets, mixins

from communications.models import Communications
from communications.serializers import CommunicationsSerializer


class CommunicationsViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    queryset = Communications.objects.all()
    serializer_class = CommunicationsSerializer
