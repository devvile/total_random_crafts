from django.shortcuts import render
from shop.models import Product
from random import randint
from admin_interface.models import PageText

def home(request):
    x = Product.objects.all().count()
    rand= randint(1,x)
    product = Product.objects.get(id=rand)
    text1 = PageText.objects.get(name='home')
    kwargs = {'product':product,'text1':text1}
    return render(request,'home/home.html',kwargs)

def about_us(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')

def delivery(request):
    return render(request,'home/delivery.html')


