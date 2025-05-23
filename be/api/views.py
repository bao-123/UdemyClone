from django.shortcuts import get_object_or_404
from api.models import Product, User, Order, OrderItem
from api.serializers import ProductSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
# Create your views here.


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    
    return Response(serializer.data)


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True, context={"request": request})

    return Response(serializer.data)