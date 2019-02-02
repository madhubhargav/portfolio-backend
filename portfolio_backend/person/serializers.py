from rest_framework import serializers

from person.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    social = serializers.HyperlinkedRelatedField(view_name='social-detail', read_only=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'url',
            'first_name',
            'middle_name',
            'last_name',
            'preferred_name',
            'social'
        )
