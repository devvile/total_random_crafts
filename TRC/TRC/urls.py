
from home.views import home, about_us, contact
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', home, name='index'),
    path('about',about_us,name='about'),
    path('contact', contact, name='contact'),
]
