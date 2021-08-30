from django.shortcuts import render
from .models import product

# Create your views here.

def products(request):
    prods=product.objects.all()
    return render(request,'product-view.html',{'prods':prods})