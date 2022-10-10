from django.contrib import admin
from .models import Product, Category, SubCategory, ProductReview

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductReview)
