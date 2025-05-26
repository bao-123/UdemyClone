from django.shortcuts import get_object_or_404
from django.db.models import Max
from api.models import Product, User, Order, OrderItem
from api.serializers import ProductSerializer, ProductInfoSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
# Create your views here.


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]

#-i Using RetrieveAPIView for getting a product based on provided pk
class ProductDetailAPIView(generics.RetrieveAPIView):
    #*The view will get the product in the base queryset (here is every Product object)
    queryset = Product.objects.all()

    serializer_class = ProductSerializer


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product", "user").all()
    serializer_class = OrderSerializer


class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product", "user").all()
    serializer_class = OrderSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

