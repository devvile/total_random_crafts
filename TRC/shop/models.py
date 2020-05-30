from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.BooleanField(default=False)
    bargain_price= models.DecimalField(blank=True,null=True, max_digits=6, decimal_places=2 )
    number = models.IntegerField(default=1)
    short_description=models.TextField(max_length=250,blank=True,null=True)
    full_description = models.TextField(max_length=500, default = ' no description')
    category = models.ManyToManyField(Category, related_name='what_category')
    thumbnail = models.ImageField(upload_to='static/img',default = None,null=True)

    def __str__(self):
        return self.name
