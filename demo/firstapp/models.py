from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
  roll = models.IntegerField(unique=True)
  name= models.CharField(max_length=255)
  email= models.EmailField(max_length=50)
  address= models.CharField(max_length=255)
  contact= models.CharField(max_length=10)

  def __str__(self):
    return self.name
  

