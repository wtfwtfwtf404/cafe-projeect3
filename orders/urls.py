from django.urls import path
from .views import create_order, get_orders

urlpatterns = [
    path("order/", create_order),
    path("orders/", get_orders),
]