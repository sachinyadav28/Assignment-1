from rest_framework import serializers
from order_app.models import Driver

class Driver(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ('id', 'name', 'phone', 'pickup_address', 'delivery_location')
        read_only_fields = ('id',)

