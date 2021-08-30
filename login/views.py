from django.shortcuts import render,redirect
from register.models import customer
import products


# Create your views here.
def login(request):
    if request.method=='POST':
        print("hello")
        email=request.POST['email']
        password=request.POST['password']
        if customer.objects.filter(email=email, password=password).count() ==1:
            request.session['email'] = email
            return redirect('products:products')


    
    else:
        return render(request,'login.html')
