from rest_framework import viewsets
from django.http import Http404

from .models import Order
from .serializers import OrderSerializer
from users.models import User


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet, реализующий CRUD операции к модели заказа."""
    queryset = Order.objects.select_related('user').all()
    serializer_class = OrderSerializer
