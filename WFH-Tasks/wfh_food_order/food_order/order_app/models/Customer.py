from djangp.db import models
from django.conf import settings

class Customer(models.Model):
    """Base model for Customer"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	city = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'order_app'

