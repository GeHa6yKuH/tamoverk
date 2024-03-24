import uuid

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=300, unique=True)
    phoneNumber = models.CharField(max_length=15, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'phoneNumber']
