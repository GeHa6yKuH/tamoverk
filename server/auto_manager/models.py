import uuid
from django.db import models


class ChecksTestResult(models.TextChoices):
    PASSED = 'PASSED'
    FAILED = 'FAILED'


class Auto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    driver_id = models.UUIDField()
    licence_plate = models.CharField(max_length=20)
    make_model = models.CharField(max_length=50)
    year = models.DateField()


class Checks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.UUIDField
    employee_id = models.UUIDField
    timestamp = models.DateTimeField
    result = models.CharField(max_length=20, choices=ChecksTestResult.choices)
    reason = models.CharField(max_length=100)
