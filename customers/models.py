from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
import datetime

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to="admins")

    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    first_name=models.CharField(max_length=12, null=True)
    last_name=models.CharField(max_length=12, null=True)
    gender_choice=(
        ('Female','Female'),
        ('Male','Male'),
        ('3','Prefer not to say')
    )
    gender=models.CharField(max_length=8,choices=gender_choice, null=True)

    email_address=models.EmailField(null=True)
    national_Id=models.CharField(max_length=20)
    description=models.TextField(max_length=299)
    attachnment=models.FileField(upload_to="documents/")
    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products")
    price=models.FloatField()
    start_date = models.DateTimeField(null=True)
    expired_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.name



class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.SET_NULL, blank=True,null=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitems= self.orderitem_set.all()
        total=sum ([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total=sum ([item.quantity for item in orderitems])
        return total




class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True, blank=True)
   


    @property
    def get_total(self):
        total=self.product.price *self.quantity
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(null=True)

    def __str__(self):
        return self.address