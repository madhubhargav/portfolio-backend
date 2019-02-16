from rest_framework import serializers

from skill.models import Skill, SkillCategory


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = (
            'id',
            'name',
        )


class SkillSerializer(serializers.ModelSerializer):
    category = SkillCategorySerializer(read_only=True)

    class Meta:
        model = Skill
        fields = (
            'id',
            'name',
            'last_used',
            'person',
            'level',
            'category',
            'icon_url',
        )
