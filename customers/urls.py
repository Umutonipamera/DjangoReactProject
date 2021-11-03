
from django.urls import path
from .import views

from .views import register_customer,product_view,store

urlpatterns=[
    path('',views.store,name="store"),
    path('view/<int:id>/',views.product_view,name="view"),
    path('cart/',views.cart,name="cart"),
    path("register/", register_customer, name="register_customer"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
]
