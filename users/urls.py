from django.urls import path, include

from . import views
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'api/v1/users', CustomUserViewSet, basename='users')
router.register(r'api/v1/user', ProfileCustomUserViewSet, basename='user')

router.register(r'api/v1/vacations', VacationsViewSet, basename='vacations')
router.register(r'api/v1/loglist', LogListViewSet, basename='loglist')
router.register(r'api/v1/mawseditstatus', MawsEditStatusViewSet, basename='mawseditstatus')
router.register(r'api/v1/formsmaws', FormsMawsViewSet, basename='formsmaws')
router.register(r'api/v1/check/(?P<id_num>.+)', CheckUserViewSet, basename='checkuser')
# router.register(r'api/v1/users/change_password/<uuid4:pk>/', CustomUserViewSet, basename='auth_change_password')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path('api/v1/user_logout/', LogoutView.as_view(), name='user_logout'),
    path('showproducts', views.show_products, name='showproducts'),
    path('create-pdf', views.pdf_report_create, name='create-pdf'),
    path('create', views.generate_pdf, name='createf'),
    path('render/pdf/', Pdf.as_view(), name='createpdf'),
]
