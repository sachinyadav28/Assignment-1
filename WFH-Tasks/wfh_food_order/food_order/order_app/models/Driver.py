from django.db import models
from django.conf import settings

class Driver(models.Model):
    """Base model for driver delivering order"""
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=10, blank=True)
    pickup_address = models.CharField(max_length=500, blank=True)
    delivery_location = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'order_app'

