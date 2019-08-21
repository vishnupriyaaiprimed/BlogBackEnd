from rest_framework import serializers
from .models import Post, Profile1
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile1
        fields="__all__"