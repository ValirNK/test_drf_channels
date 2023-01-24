from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Product, Client, Type

class ProductSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()
    # invited = UserSerializer(many=True)
    class Meta:
        model = Product
        fields = ("id", "name", "price", "currency", 'in_stock', 'code', 'image', 'date_update', 'type_product', 'manufacturer')
        depth = 1

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ("id", "name", "description")

class ClientSerializer(serializers.ModelSerializer):
    cart = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Client
        fields = ("id", "name", "adress", "cart")