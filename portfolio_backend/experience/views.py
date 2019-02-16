from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend
from experience.models import Experience, ExperienceDescription
from experience.serializers import ExperienceSerializer, ExperienceDescriptionSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('person',)
    ordering_fields = ('start_date',)

    def get_queryset(self):
        if 'person' in self.request.query_params:
            return Experience.objects.all()
        return Experience.objects.none()


class ExperienceDescriptionViewSet(viewsets.ModelViewSet):
    queryset = ExperienceDescription.objects.all()
    serializer_class = ExperienceDescriptionSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('experience',)
    ordering_fields = ('priority',)

    def get_queryset(self):
        if 'experience' in self.request.query_params:
            return ExperienceDescription.objects.all()
        return ExperienceDescription.objects.none()
