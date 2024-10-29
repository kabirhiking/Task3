# restaurant/views.py

from django.shortcuts import render
from .models import MenuItem, Order, Reservation, Inventory

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/order_list.html', {'orders': orders})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'restaurant/reservation_list.html', {'reservations': reservations})

def inventory_list(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'restaurant/inventory_list.html', {'inventory_items': inventory_items})
