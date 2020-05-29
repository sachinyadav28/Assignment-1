from django.db import models
from order_app.models import Restaurant

def upload_menu_image(instance, filename):
    return "image/{menu}/{filename}".format(menu=instance.menu, filename=filename)

class Menu(models.Model):
    """Model for the food items restaurant have"""
    
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=upload_menu_image, null=True, blank=True)

    def __str__(self):
        return self.item_name

    class Meta:
        app_label = 'order_app'

        