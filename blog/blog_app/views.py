from django.shortcuts import render
from .models import Posst
from django.contrib.auth.models import User
from .serializers import PostSerializer,UserSerializer
from rest_framework import viewsets

# Create your views here.

class UserViewSetByUsername(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field='username'

class PostViewSet(viewsets.ModelViewSet):
    queryset=Posst.objects.all().order_by('-date','-time')
    serializer_class=PostSerializer
