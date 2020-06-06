from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required

def shop(request):
    list_of_products = Product.objects.all().order_by('-timestamp')
    categories= Category.objects.all()
    kwargs = {'list_of_products': list_of_products, 'categories': categories}
    return render(request, 'shop/shop.html', kwargs)


def detail(request, id):
    product = Product.objects.get(id=id)
    kwargs = {'product': product}
    return render(request, 'shop/detail.html', kwargs)

def category(request, name):
    category = Category.objects.get(name=name)
    kwargs = {'category': category}
    return render(request, 'shop/categories.html', kwargs)

@login_required
def admin_site(request):
    return render(request,'shop/admin_site.html')

@login_required
def cart(request):
    return render(request,'shop/admin_site.html')


@login_required
def new_product(request):
    pass