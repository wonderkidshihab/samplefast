from django.test import TestCase

# Create your tests here.
from product.models import Category, SubCategory, Product, ProductReview
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create
        name='Shoes'
        description='The best shoes in the world'
        image='static/category/shoes.png'
        slug='shoes'
        Category.objects.create(name=name, description=description, image=image, slug=slug)
        
    def test_category(self):
        shoes = Category.objects.get(name='Shoes')
        self.assertEqual(shoes.name, 'Shoes')
        self.assertEqual(shoes.description, 'The best shoes in the world')
        self.assertEqual(shoes.image, 'static/category/shoes.png')
        self.assertEqual(shoes.slug, 'shoes')