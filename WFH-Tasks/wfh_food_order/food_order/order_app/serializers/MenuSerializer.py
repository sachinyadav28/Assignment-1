from rest_framework import serializers
from order_app.models import Menu
from order_app.serializers import RestaurantSerializer

class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        fields = ('id','restaurant', 'item_name', 'short_description', 'price', 'image')
        read_only_fields = ('id',)

    def validate(self, data):
        short_description = data.get("short_description", None)
        if short_description == "":
            short_description = None
        image = data.get("image", None)
        if short_description is None and image is None:
            raise serializers.ValidationError("short_description or image is required.")
        return data