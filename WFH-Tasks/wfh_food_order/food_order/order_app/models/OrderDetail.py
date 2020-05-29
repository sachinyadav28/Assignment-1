from django.db import models
from order_app.models import Order, Menu

class OrderDetail(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    meal = models.ForeignKey('Menu', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.order

    class Meta:
        app_label = 'order_app'
