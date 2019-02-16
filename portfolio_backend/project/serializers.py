from rest_framework import serializers

from project.models import Project, ProjectDescription


class ProjectDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDescription
        fields = (
            'id',
            'description',
            'priority',
        )


class ProjectSerializer(serializers.ModelSerializer):
    descriptions = ProjectDescriptionSerializer(
        many=True,
        read_only=True,
        source='project_descriptions'
    )

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'short_description',
            'start_date',
            'end_date',
            'academy',
            'person',
            'descriptions',
        )
