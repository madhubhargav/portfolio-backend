from rest_framework import serializers

from social.models import Social


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = (
            'phone',
            'email',
            'linkedin',
            'github',
            'twitter',
            'facebook',
            'discord',
            'person'
        )
