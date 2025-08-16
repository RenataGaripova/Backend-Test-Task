from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import OrderViewSet

# Регистрируем вьюсеты для работы с заказами.

orders_router = SimpleRouter()

orders_router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(orders_router.urls)),
]
