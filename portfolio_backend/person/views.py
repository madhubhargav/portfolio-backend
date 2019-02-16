from rest_framework import viewsets

from person.models import Person
from person.serializers import PersonSerializer


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.filter(last_name='Pallem')
    serializer_class = PersonSerializer
