from django.shortcuts import render
from shop.models import Product, Category
from shop.forms import ProductForm, CategoryForm

def add_page(request):
    form1 = ProductForm
    context = {'form1':form1}
    return render(request,'admin/add.html',context)

def stats_page(request):
    return render(request,'admin/stats.html')

def categories(request):
    form2 = CategoryForm
    context = {'form2':form2}
    return render(request,'admin/categories.html',context)



def all_products(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {'product_list':product_list,'category_list':category_list}
    return render(request,'admin/all_products.html', context)


def orders_list(request):
    return render(request,'admin/orders_list.html')

def edit_pages(request):
    return render(request,'admin/edit_pages.html')


def edit_data(request):
    return render(request,'admin/edit_data.html')

