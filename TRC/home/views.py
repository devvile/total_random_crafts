from django.shortcuts import render
from shop.models import Product
from random import randint

def home(request):
    x = Product.objects.all().count()
    rand= randint(1,x)
    product = Product.objects.get(id=rand)
    kwargs = {'product':product}
    return render(request,'home/home.html',kwargs)

def about_us(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')