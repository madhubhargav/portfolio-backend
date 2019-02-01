from rest_framework import serializers

from people.models import People


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = (
            'id',
            'url',
            'first_name',
            'middle_name',
            'last_name',
            'preferred_name'
        )
