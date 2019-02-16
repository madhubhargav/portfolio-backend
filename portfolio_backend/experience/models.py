import uuid
from django.db import models
from django.core.validators import MaxValueValidator

from person.models import Person


class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    designation = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class ExperienceDescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    priority = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(15)])
    description = models.TextField(max_length=400)

    def __str__(self):
        return '{0} {1}'.format(self.priority, self.description)
