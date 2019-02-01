from rest_framework import serializers

from communications.models import Communications


class CommunicationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Communications
        fields = (
            'id',
            'phone',
            'email',
            'linkedin',
            'github',
            'twitter',
            'facebook',
            'discord',
            'people'
        )
