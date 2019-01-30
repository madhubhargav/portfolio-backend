import uuid
from django.db import models


class People(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    preferred_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
