from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# Create your models here.


class Role(models.TextChoices):
    CUSTOMER = "CUSTOMER"
    MASTER = "Master"


class User(AbstractUser):
    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

    email = models.EmailField(
        "Email Address",
        unique=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']