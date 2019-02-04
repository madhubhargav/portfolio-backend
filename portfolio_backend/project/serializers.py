from rest_framework import serializers

from project.models import Project, ProjectDescription


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    project_descriptions = serializers.HyperlinkedRelatedField(
        view_name='projectdescription-detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Project
        fields = (
            'id',
            'url',
            'name',
            'short_description',
            'start_date',
            'end_date',
            'academy',
            'person',
            'project_descriptions',
        )


class ProjectDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectDescription
        fields = (
            'id',
            'url',
            'description',
            'priority',
        )
