from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)  # auto-generate token
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers', 'following']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
            token = Token.objects.create(user=user)
        return user, token