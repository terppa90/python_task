from rest_framework import serializers
from .models import CartItem
import json

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=20)


class ProductSerializer(serializers.ModelSerializer):
    """Serializes a name field for testing our APIView"""
    class Meta:
        model=CartItem
        fields=['name', 'price']