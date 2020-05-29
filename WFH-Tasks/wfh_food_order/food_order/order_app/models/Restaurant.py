from djangp.db import models
from django.conf import settings

def upload_restaurant_logo(instance, filename):
    return "logo/{restaurant}/{filename}".format(restaurant=instance.restaurant, filename=filename)

class Restaurant(models.Model):
    """Base model for restaurant"""
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length = 500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to=upload_restaurant_logo, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'order_app'

