from rest_framework import serializers

from experience.models import Experience, ExperienceDescription


class ExperienceDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = (
            'id',
            'experience',
            'priority',
            'description',
        )


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    descriptions = ExperienceDescriptionSerializer(
        many=True,
        read_only=True,
        source='experiencedescription_set'
    )

    class Meta:
        model = Experience
        fields = (
            'id',
            'url',
            'person',
            'company_name',
            'location',
            'designation',
            'start_date',
            'end_date',
            'descriptions',
        )
