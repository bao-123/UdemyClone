from rest_framework import serializers
from .models import Product, User, Order, OrderItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "stock")
    

    def validate_price(self, value):
        if value <=0 :
            raise serializers.ValidationError("price must be greate than zero")
        return value
    

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(view_name="product_info", read_only=True)

    class Meta:
        model = OrderItem
        fields = ("product", "quantity", "subtotal_price")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    total_price = serializers.SerializerMethodField(method_name="total")

    def total(self, obj):
        total_price = 0
        items = obj.items.all()
        for item in items:
            total_price += item.subtotal_price
        
        return total_price
        
    class Meta:
        model = Order
        fields = ("order_id", "status", "created_at", "user", "items", "total_price")
    

class ProductInfoSerializer(serializers.Serializer):
    #*get all products, count of product and max_price
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    