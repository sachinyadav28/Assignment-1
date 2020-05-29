from django.db import models
from order_app.models import Customer, Restaurant, Driver
from order_app.enums import OrderStatus

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, blank = True, null = True)
    delivery_address = models.CharField(max_length=500)
    total_price = models.PositiveIntegerField()
    status = models.CharField(max_length=1, default=OrderStatus.WAITING, choices=OrderStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer

    class Meta:
        app_label = 'order_app'

        