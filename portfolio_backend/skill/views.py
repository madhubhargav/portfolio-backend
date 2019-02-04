from rest_framework import viewsets, mixins, filters

from django_filters.rest_framework import DjangoFilterBackend
from skill.models import Skill, SkillCategory
from skill.serializers import SkillSerializer, SkillCategorySerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('person', 'level', 'category')
    ordering_fields = ('last_used', 'level', 'category')

    def get_queryset(self):
        if 'person' in self.request.query_params:
            return Skill.objects.all()
        return Skill.objects.none()


class SkillCategoryViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
