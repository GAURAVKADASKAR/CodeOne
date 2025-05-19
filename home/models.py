from django.db import models
from django.contrib.auth.models import User

# Model for the registration for the user
class UserRegistraion(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    isadmin=models.BooleanField(default=False)
    isuser=models.BooleanField(default=False)
    isactive = models.BooleanField(default=False)
    isverified = models.BooleanField(default=False)
    password = models.TextField()

    def __str__(self):
        return self.username





