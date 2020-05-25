from .models import Category, Product
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        Fields = ['name']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        Fields = ['name','price','discount','bargain_price','number','short_description','full_description','category']

