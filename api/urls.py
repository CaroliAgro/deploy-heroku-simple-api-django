from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProductViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]