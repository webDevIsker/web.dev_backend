from django.urls import path, include
from .views import PriceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/prices', PriceViewSet, basename='prices')

urlpatterns = [
    path('', include(router.urls)),
]
