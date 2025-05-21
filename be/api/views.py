from django.shortcuts import render
from django.http import JsonResponse
from api.models import Product
from api.serializers import ProductSerializer

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return JsonResponse({
        "data": serializer.data
    }) 