from django.shortcuts import get_object_or_404
from django.db.models import Max
from api.models import Product, User, Order, OrderItem
from api.serializers import ProductSerializer, ProductInfoSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
# Create your views here.


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        "products": products,
        "count": products.count(),
        "max_price": products.aggregate(max_price=Max("price"))["max_price"]
    })

    return Response(serializer.data)


@api_view(["GET"])
def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    
    return Response(serializer.data)


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.prefetch_related("user", "items", "items__product").all()
    serializer = OrderSerializer(orders, many=True, context={"request": request})

    return Response(serializer.data)