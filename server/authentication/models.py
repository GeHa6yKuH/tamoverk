import uuid

from django.db import models


class EmployeePosition(models.TextChoices):
    INSPECTOR = 'INSPECTOR'
    SUPERVISOR = 'SUPERVISOR'
    DOCUMENTVERIFIER = 'DOCUMENTVERIFIER'


class Status(models.TextChoices):
    PENDING = 'PENDING'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


class Employee(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )

    email = models.EmailField(max_length=300, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=72)
    password = models.CharField(max_length=56)
    location = models.CharField(max_length=250)
    position = models.CharField(
            max_length=20,
            choices=EmployeePosition.choices
    )


class Authentications(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    auth_code = models.IntegerField()
    status = models.CharField(
            max_length=10,
            choices=Status.choices
    )
    timestamp = models.DateTimeField(auto_now=True)
