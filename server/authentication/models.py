import uuid

from django.db import models


class EmployeePosition(models.TextChoices):
    INSPECTOR = 'INSPECTOR'
    SUPERVISOR = 'SUPERVISOR'
    DOCUMENT_VERIFIER = 'DOCUMENTVERIFIER'


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=300, unique=True)
    phoneNumber = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=72)
    password = models.CharField(max_length=56)
    location = models.CharField(max_length=250)
    position = models.CharField(max_length=20, choices=EmployeePosition.choices)
