from rest_framework import viewsets, permissions
from .serializers import ProductsSerializer, ProductsGroupSerializer
from .models import Products, ProductsGroup


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductsGroupViewSet(viewsets.ModelViewSet):
    queryset = ProductsGroup.objects.all()
    serializer_class = ProductsGroupSerializer
    permission_classes = [permissions.IsAdminUser]