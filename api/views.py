from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from customers.models import Customer
from customers.models import Product
from customers.models import  Order
from customers.models import  OrderItem

from .serializers import CustomerSerializer
from .serializers import ProductSerializer
from .serializers import OrderSerializer
from .serializers import OrderItemSerializer



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer