import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from people.models import People


class Communications(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = PhoneNumberField()
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    people = models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
