from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from product.models import Product
# Create your views here.

class Productset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()