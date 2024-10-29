# restaurant/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('orders/', views.order_list, name='order_list'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('inventory/', views.inventory_list, name='inventory_list'),
]
