from django.shortcuts import redirect, render
from django.urls.conf import include
from .models import customer

# Create your views here.
def signup(request):
    if request.method=='POST':
        print("hello")


    return render(request,'signup.html')