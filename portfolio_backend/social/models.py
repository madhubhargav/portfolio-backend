import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from person.models import Person


class Social(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = PhoneNumberField()
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    address = models.TextField(max_length=250)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    discord = models.URLField(blank=True, null=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.email)
