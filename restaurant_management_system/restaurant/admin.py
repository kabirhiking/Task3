# restaurant/admin.py

from django.contrib import admin
from .models import MenuItem, Order, Reservation, Inventory

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(Inventory)
