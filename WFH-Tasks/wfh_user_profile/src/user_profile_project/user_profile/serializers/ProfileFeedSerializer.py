from rest_framework import serializers
from user_profile.models import ProfileFeed

class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = ProfileFeed
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}