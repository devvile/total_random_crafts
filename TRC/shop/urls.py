from django.urls import path
from .views import shop, detail, category,admin_site, cart

urlpatterns = [
    path('', shop,name = 'shop'),
    path('detail/<int:id>',detail,name='detail'),
    path('category/<str:name>',category,name='shop_category'),
    path('admin',admin_site,name='shop_admin'),
    path('cart', cart, name='cart'),

]
