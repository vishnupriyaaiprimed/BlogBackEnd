from django.shortcuts import render
from .models import Post, Profile1
from django.contrib.auth.models import User
from .serializers import PostSerializer,UserSerializer, ProfileSerializer
from rest_framework import viewsets

# Create your views here.

class UserViewSetByUsername(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field='username'

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-date','-time')
    serializer_class=PostSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile1.objects.all()
    serializer_class=ProfileSerializer
    lookup_field='user'
