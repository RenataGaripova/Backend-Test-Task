# Backend-Test-Task
Серверное приложение на Django + PostgreSQL + Docker, разработанное в рамках тестового задания Backend Developer.

#### Описание маршрутов
*   Users
    *   GET api-users/users/ - получить список пользователей.
    *   POST api-users/users/ - создать нового пользователя.
    *   GET api-users/users/<int:user_id> - получить пользователя по id.
    *   PUT, PATCH api-users/users/<int:user_id> - обновить информацию о пользователе по id.
    *   DELETE api-users/users/<int:user_id> - удалить информацию о пользователе по id.
*   Orders
    *   GET api-orders/orders/ - получить список заказов.
    *   POST api-orders/orders/ - добавить новый заказ.
    *   GET api-orders/orders/<int:order_id> - получить заказ по id.
    *   PUT, PATCH api-orders/orders/<int:order_id> - обновить информацию о заказе по id.
    *   DELETE api-orders/orders/<int:order_id> - удалить информацию о заказе по id.
#### Установка и запуск проекта:
1. Клонировать репозиторий:
```
git clone https://github.com/RenataGaripova/Backend-Test-Task.git
cd test_task
```
2. Создать .env файл (пример в .env.example)
3. Собрать и запустить контейнеры с Докер:
```
docker-compose up --build
```
4. Применить миграции и создать суперпользователя:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
5. Приложение будет доступно по адресу: http://localhost:8000
