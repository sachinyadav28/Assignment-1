from rest_framework import serializers
from order_app.models import Order
from order_app.serializers import CustomerSerializer, RestaurantSerializer, DriverSerializer

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'restaurant', 'driver', 'delivery_address', 
                'total_price', 'status', 'created_at')
        read_only_fields = ('id',)

