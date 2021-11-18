from django.urls import path, include
from .views import ProductsViewSet, ProductsGroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/products', ProductsViewSet, basename='products')
router.register(r'api/v1/products_group', ProductsGroupViewSet, basename='products_group')

urlpatterns = [
    path('', include(router.urls)),
]
