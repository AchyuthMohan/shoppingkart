from django.db import models

# Create your models here.
class customer(models.Model):
    state=models.TextField()
    password=models.CharField(max_length=20, default=None)
    address=models.TextField()
    address2=models.TextField()
    email=models.EmailField()
    city=models.TextField()