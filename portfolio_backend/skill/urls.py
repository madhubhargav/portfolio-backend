from rest_framework import routers

from skill.views import SkillViewSet, SkillCategoryViewSet


SKILL_ROUTER = routers.DefaultRouter()
SKILL_ROUTER.register(r'skill', SkillViewSet)

SKILL_CATEGORY_ROUTER = routers.DefaultRouter()
SKILL_CATEGORY_ROUTER.register(r'skill-category', SkillCategoryViewSet)
