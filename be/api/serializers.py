from rest_framework import serializers
from .models import Product, User, Order, OrderItem


class ProductSerializer(serializers.Serliazer):
    class Meta:
        model = Product
        fields = ("name", "description", "price", "created_at", "stock", "in_stock")