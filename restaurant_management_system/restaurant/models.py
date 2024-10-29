
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(MenuItem)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for Table {self.table_number}"


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    reservation_time = models.DateTimeField()
    
    def __str__(self):
        return f"Reservation for {self.name} at Table {self.table_number}"


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name
