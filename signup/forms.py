from django.forms import ModelForm
from .models import Customer
class Todoform(ModelForm):
    class  Meta:
        model=Customer
        fields=['email','password','state','address','city']