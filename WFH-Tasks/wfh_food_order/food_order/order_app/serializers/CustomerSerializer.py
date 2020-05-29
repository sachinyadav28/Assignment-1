from rest_framework import serializers
from order_app.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ('id', 'name', 'city', 'phone', 'address')
        read_only_fields = ('id',)

