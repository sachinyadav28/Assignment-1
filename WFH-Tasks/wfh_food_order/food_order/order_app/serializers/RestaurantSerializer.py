from rest_framework import serializers
from order_app.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'phone', 'address', 'logo')
        read_only_fields = ('id',)

        