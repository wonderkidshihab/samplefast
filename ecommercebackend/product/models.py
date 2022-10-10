from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category', null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='subcategory', null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='product', null=True, blank=True)
    images = ArrayField(models.ImageField(upload_to='product', null=True, blank=True), size=5, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    size = ArrayField(models.CharField(max_length=10), null=True, blank=True)
    color = ArrayField(models.CharField(max_length=10), null=True, blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class ProductReview(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    review = models.TextField()
    rating = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


