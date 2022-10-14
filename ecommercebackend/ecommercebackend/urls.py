from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product', include('product.urls')),
    path('api/cart', include('cart.urls')),
    
]
