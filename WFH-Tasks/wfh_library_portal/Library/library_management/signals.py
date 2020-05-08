from django.db.models.signals import pre_save
from django.dispatch import receiver

from library_management.models import Books

@receiver(pre_save, sender=Books)
def make_available(instance, **kwargs):
    if instance.quantity == 0:
        instance.available = False
    else:
        instance.available = True
    
    