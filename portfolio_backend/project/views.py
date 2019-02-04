from rest_framework import viewsets, mixins, filters

from django_filters.rest_framework import DjangoFilterBackend
from project.models import Project, ProjectDescription
from project.serializers import ProjectDescriptionSerializer, ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('person',)
    ordering_fields = ('start_date', 'end_date')

    def get_queryset(self):
        if 'person' in self.request.query_params:
            return Project.objects.all()
        return Project.objects.none()


class ProjectDescriptionViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    basename = 'project-description'
    queryset = ProjectDescription.objects.all().order_by('priority')
    serializer_class = ProjectDescriptionSerializer
