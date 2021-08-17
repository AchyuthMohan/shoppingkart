from django.db import models

# Create your models here.
class product(models.Model):
    price=models.IntegerField()
    name=models.CharField(max_length=100)
    desc=models.TextField()
    release_date=models.DateField()
    img=models.ImageField(upload_to='pics')