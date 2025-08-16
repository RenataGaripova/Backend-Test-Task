from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet

# Регистрируем вьюсеты для работы с пользователями.

users_router = SimpleRouter()

users_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(users_router.urls)),
]
