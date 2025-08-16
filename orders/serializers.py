from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя."""
    class Meta:
        model = Order
        fields = ('id', 'name', 'description', 'user')
