from rest_framework import viewsets, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from catalogs.models import Products
from .permissions import IsAdminOrReadOnly
from .serializers import PricesSerializer
from .models import Prices
import django_filters


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='product__full_name', lookup_expr='contains')

    class Meta:
        fields = ['products__full_name']


class StandartResultPagePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'per_page': self.page.paginator.per_page,
            'result': data,
        })


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = StandartResultPagePagination
    filterset_class = ProductFilter

    def create(self, request, *args, **kwargs):
        try:
            product = Products.objects.filter(pk=request.data['product']).get()
            price = request.data['price']
            if product:
                if price == 0:
                    self.queryset.filter(product=product).delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    product_price = self.queryset.filter(product=product)
                    if product_price:
                        obj = product_price.get()
                        obj.price = price
                        obj.save()
                        return Response(status=status.HTTP_206_PARTIAL_CONTENT)
                    else:
                        obj = self.queryset.create(product=product, price=price)
                        obj.save()
                        return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(data={"error": ex.__str__}, status=status.HTTP_400_BAD_REQUEST)
