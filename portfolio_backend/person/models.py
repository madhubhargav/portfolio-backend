import uuid
from django.db import models


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    preferred_name = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
