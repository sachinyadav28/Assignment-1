from rest_framework import serializers
from order_app.models import OrderDetail
from order_app.serializers import OrderSerializer, MenuSerializer

class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    meal = MenuSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'meal', 'quantity')
        read_only_fields = ('id',)

