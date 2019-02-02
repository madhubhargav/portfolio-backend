from rest_framework import viewsets

from person.models import Person
from person.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('first_name', 'last_name')
    serializer_class = PersonSerializer
