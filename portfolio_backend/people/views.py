from rest_framework import viewsets

from people.models import People
from people.serializers import PeopleSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all().order_by('first_name', 'last_name')
    serializer_class = PeopleSerializer
