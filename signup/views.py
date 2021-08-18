from signup.forms import Todoform
from django.shortcuts import redirect, render
from django.urls.conf import include
from .models import Customer
from django.contrib.auth.models import User


# Create your views here.
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')

    if request.method=='POST':
         user=User.objects.create_user(request.POST['email'],password=request.POST['password'])
         form=Todoform(request.POST)
         if form.is_valid():
             newtodo=form.save(commit=False)
             newtodo.user=request.user
             newtodo.save() 
         if form.errors():
             pass         
         user.save()
         