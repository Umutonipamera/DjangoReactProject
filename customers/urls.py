
from django.urls import path
from .import views

from .views import register_customer

urlpatterns=[
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path("register/", register_customer, name="register_customer"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
]
