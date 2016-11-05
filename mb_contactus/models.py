from django.db import models
from mb_database.fields import UUIDField

class ContactUsQuestion(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    first_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    email = models.CharField(max_length=100, default=None, blank=True, null=True)
    question = models.CharField(max_length=100, default=None, blank=True, null=True)

