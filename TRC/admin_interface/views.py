from django.shortcuts import render, redirect
from shop.models import Product, Category
from shop.forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def add_page(request):
    form1 = ProductForm
    context = {'form1':form1}
    return render(request,'admin/add.html',context)


@login_required
def stats_page(request):
    return render(request,'admin/stats.html')


@login_required
def categories(request):
    form2 = CategoryForm
    context = {'form2':form2}
    return render(request,'admin/categories.html',context)


@login_required
def all_products(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {'product_list':product_list,'category_list':category_list}
    return render(request,'admin/all_products.html', context)



@login_required
def orders_list(request):
    return render(request,'admin/orders_list.html')


@login_required
def edit_pages(request):
    return render(request,'admin/edit_pages.html')


def edit_data(request):
    return render(request,'admin/edit_data.html')


@login_required
def new_product(request):
        if request.method == "POST":
            nowy =  Product(timestamp= timezone.now())
            form1 = ProductForm(instance = nowy,data=request.POST)
            if form1.is_valid():
                form1.save()
                return redirect("index")
        return redirect("shop_admin")
