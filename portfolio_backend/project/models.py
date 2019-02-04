import uuid
from django.db import models

from person.models import Person


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    academy = models.BooleanField()
    short_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class ProjectDescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=300)
    priority = models.PositiveIntegerField()
    project = models.ForeignKey(
        Project,
        related_name='project_descriptions',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)
