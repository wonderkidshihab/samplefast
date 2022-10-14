from rest_framework import serializers
from .models import Cart, CartProduct
from product.serializers import ProductSerializer

class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartProduct
        fields = ['product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['products']
