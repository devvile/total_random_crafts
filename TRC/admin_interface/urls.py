from django.urls import path

from . import views

urlpatterns = [path('add',views.add_page,name='add_page'),
               path('stats',views.stats_page, name = 'stats_page'),
               path('all_products', views.all_products,name='all_products'),
               path('orders_list',views.orders_list,name='orders_list_page'),
               path('edit_pages',views.edit_pages,name ='edit_pages'),
               path('edit_data',views.edit_data,name='edit_data'),
               path('create', views.new_product, name='new_product'),
path('categories',views.categories,name='categories')


]