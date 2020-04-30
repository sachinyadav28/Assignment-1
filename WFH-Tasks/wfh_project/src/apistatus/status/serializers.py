from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from user.jwt.serializers import UserPublicSerializer
from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    user            = UserPublicSerializer(read_only=True)

    class Meta:
        model = Status 
        fields =[
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user'] # GET  #readonly_fields

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-status:detail', kwargs={"id": obj.id}, request=request)

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


class StatusInlineUserSerializer(StatusSerializer):
    class Meta:
        model = Status 
        fields =[
            'uri',
            'id',
            'content',
            'image'
        ]

