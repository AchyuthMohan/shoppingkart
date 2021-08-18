from django.db import models

# Create your models here.
class Customer(models.Model):
    state=models.CharField(max_length=200)
    password=models.CharField(max_length=200, default=None)
    address=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    city=models.CharField(max_length=200)