import uuid
from django.db import models
from django.core.validators import MaxValueValidator

from person.models import Person


class SkillCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    last_used = models.DateField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
    category = models.ForeignKey(SkillCategory, on_delete=models.SET_NULL, null=True)
    icon_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
