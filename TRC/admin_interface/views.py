from django.shortcuts import render
from shop.models import Product

def add_page(request):
    return render(request,'admin/add.html')

def stats_page(request):
    return render(request,'admin/stats.html')


def all_products(request):
    product_list = Product.objects.all()
    context = {'product_list':product_list}
    return render(request,'admin/all_products.html', context)


def orders_list(request):
    return render(request,'admin/orders_list.html')

def edit_pages(request):
    return render(request,'admin/edit_pages.html')


def edit_data(request):
    return render(request,'admin/edit_data.html')

