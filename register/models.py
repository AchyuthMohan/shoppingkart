from django.db import models
from django.db.models.base import Model

# Create your models here.
class customer(models.Model):
    email=models.EmailField()
    name=models.TextField()
    address=models.TextField()
    address2=models.TextField()
    city=models.TextField()
    state=models.TextField()
    password=models.TextField()