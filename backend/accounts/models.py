from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='admin','Admin',
        MANAGER='manager','Manager',
        EMPLOYEE='employee','Employee'

    role=models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.EMPLOYEE
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
    