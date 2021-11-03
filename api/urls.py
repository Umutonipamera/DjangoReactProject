
from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet
from .views import ProductViewSet
from .views import OrderViewSet
from .views import OrderItemViewSet


router = routers.DefaultRouter()
router.register("customers/",CustomerViewSet)

router.register("products/",ProductViewSet)
router.register("orders/",OrderViewSet)
router.register("orderItems/",OrderItemViewSet)



urlpatterns = [
    path("",include(router.urls)),
]