from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=500, null=False, blank=False)
    email = models.EmailField(unique=True)

    # Set 'email' as the unique identifier for authentication
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.email
