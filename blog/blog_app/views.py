from django.shortcuts import render
from .models import Posst
from .serializers import PostSerializer
from rest_framework import viewsets

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Posst.objects.all()
    serializer_class=PostSerializer
