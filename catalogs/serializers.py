import uuid

from rest_framework import serializers
from .models import Products, ProductsGroup


class ProductsSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)

    class Meta:
        model = Products
        fields = ['id', 'full_name', 'group']


class ProductsGroupSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)

    class Meta:
        model = ProductsGroup
        fields = ['id', 'title', 'parent']