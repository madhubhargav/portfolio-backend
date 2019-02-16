from rest_framework import serializers

from person.models import Person
from social.serializers import SocialSerializer
from experience.serializers import ExperienceSerializer
from project.serializers import ProjectSerializer
from skill.serializers import SkillSerializer


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    social = SocialSerializer(read_only=True)
    experiences = ExperienceSerializer(
        many=True,
        read_only=True,
        source='experience_set'
    )
    projects = ProjectSerializer(
        many=True,
        read_only=True,
        source='project_set'
    )
    skills = SkillSerializer(
        many=True,
        read_only=True,
        source='skill_set'
    )

    class Meta:
        model = Person
        fields = (
            'id',
            'url',
            'first_name',
            'middle_name',
            'last_name',
            'preferred_name',
            'image_url',
            'description',
            'social',
            'experiences',
            'projects',
            'skills',
        )
