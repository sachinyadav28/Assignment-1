from django.db import models
from django.utils.translation import gettext_lazy as _

class OrderStatus(models.TextChoices):
    WAITING = 'WT', _('Waiting')
    ACCEPTED = 'AC', _('Accepted')
    CANCELLED = 'CN', _('Cancelled')
    COOKING = 'CK', _('Cooking')
    ONTHEWAY = 'OW', _('On The Way')
    DELIVERED = 'DL' _('Delivered')
