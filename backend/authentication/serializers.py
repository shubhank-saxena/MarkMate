from rest_framework import serializers
from backend.authentication.models import User
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)

        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise serializers.ValidationError('Email addresses must be unique.')
        
        if username and User.objects.filter(username=username).exclude(email=email).exists():
            raise serializers.ValidationError('Usernames must be unique.')
        
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters.')
        
        if len(username) < 6:
            raise serializers.ValidationError('The username should be at least 6 characters long.')
        
        if len(username) > 20:
            raise serializers.ValidationError('The username should be at most 20 characters long.')

        return data

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, min_length=8)
    username = serializers.CharField(read_only=True)
    tokens = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'tokens' )

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid credentials. Please try again.')
        
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }
