from django.db import models


class User(models.Model):
    """Модель пользователя."""
    name = models.CharField(
        max_length=256,
    )
    email = models.CharField(
        max_length=256,
    )
    age = models.PositiveSmallIntegerField(
    )
