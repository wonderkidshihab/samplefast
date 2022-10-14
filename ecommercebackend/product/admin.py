from django.contrib import admin
from .models import Product, Category, SubCategory, ProductReview

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(ProductReview)


# create inlines for category and subcategory


    
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0
    classes = ['collapse']
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SubCategoryInline]
    
class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    classes = ['collapse']
    inlines = [CategoryAdmin]
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
admin.site.register(Product)

