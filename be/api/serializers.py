from rest_framework import serializers
from .models import Product, User, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "price", "stock")
    

    def validate_price(self, value):
        if value <=0 :
            raise serializers.ValidationErro("price must be greate than zero")
        return value