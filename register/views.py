from django.shortcuts import redirect, render
from django.urls.conf import include

from .models import customer


# Create your views here.
def register(request):
    if(request.method=='POST'):
        email=request.POST['email']
        address=request.POST['address']
        address2=request.POST['address2']
        password=request.POST['password']
        state=request.POST['state']
        city=request.POST['city']


        c=customer(email=email,address=address,address2=address2,password=password,state=state,city=city)
        c.save();
        
        return redirect('/')
        
    else:
        return render(request,'signup.html')