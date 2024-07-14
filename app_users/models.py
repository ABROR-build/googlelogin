from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username
