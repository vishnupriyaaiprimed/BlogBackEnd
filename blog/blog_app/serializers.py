from rest_framework import serializers
from .models import Posst

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posst
        fields="__all__"