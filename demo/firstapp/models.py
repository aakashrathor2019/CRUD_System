from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    roll = models.IntegerField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.username
