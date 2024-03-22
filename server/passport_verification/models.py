import uuid
from django.db import models


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=72)
    document_number = models.CharField(max_length=15)
    date = models.DateTimeField()
