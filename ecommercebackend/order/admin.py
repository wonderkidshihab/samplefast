from django.contrib import admin
from .models import Order, OrderProduct, ShippingAddress, Payment
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(ShippingAddress)
admin.site.register(Payment)
