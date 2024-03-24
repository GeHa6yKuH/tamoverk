import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=300, unique=True)
    phoneNumber = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=72)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'phoneNumber', 'password']
