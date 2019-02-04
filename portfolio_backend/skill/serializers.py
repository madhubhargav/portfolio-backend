from rest_framework import serializers

from skill.models import Skill, SkillCategory


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = (
            'id',
            'url',
            'name',
            'last_used',
            'person',
            'level',
            'category',
            'icon_url',
        )


class SkillCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillCategory
        fields = (
            'id',
            'url',
            'name',
        )
