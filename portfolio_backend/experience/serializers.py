from rest_framework import serializers

from experience.models import Experience, ExperienceDescription


class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = (
            'id',
            'experience',
            'priority',
            'description',
        )


class ExperienceSerializer(serializers.ModelSerializer):
    descriptions = ExperienceDescriptionSerializer(
        many=True,
        read_only=True,
        source='experiencedescription_set'
    )

    class Meta:
        model = Experience
        fields = (
            'id',
            'person',
            'company_name',
            'location',
            'designation',
            'start_date',
            'end_date',
            'descriptions',
        )
