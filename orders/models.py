from django.db import models

from users.models import User


class Order(models.Model):
    """Модель заказа."""

    name = models.CharField(max_length=256)
    description = models.TextField()
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
