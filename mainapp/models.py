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

class product(models.Model):
    price=models.IntegerField()
    name=models.CharField(max_length=100)
    desc=models.TextField()
    release_date=models.DateField()
    img=models.ImageField(upload_to='pics')