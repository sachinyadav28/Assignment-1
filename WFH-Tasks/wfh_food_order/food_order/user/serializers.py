from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = User
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def get_message(self, obj):
        return "Thank you for registering. Please verify your email before continuing."
    
    def validate_email(self, value):
        email = User.objects.filter(email__iexact=value)
        if email.exists():
            raise serializers.ValidationError("User with this email already exists")
        return value

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, validated_data):
        """Validate and authenticate the user"""
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError('Unable to authenticate with provided credentials', code='authentication')

        validated_data['user'] = user
        return validated_data