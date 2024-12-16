from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=500, null=False, blank=False)
    username = models.CharField(max_length=500, unique= True)
    email = models.EmailField(unique=True)

    # Set 'email' as the unique identifier for authentication
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
