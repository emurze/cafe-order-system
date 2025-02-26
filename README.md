# Cистема управления заказами в кафе

Перед установкой, убедитесь, пожалуйста, что у вас установлен докер.

### Инструктция по установке

1. Скачам git репозиторий

```
git clone git@github.com:emurze/cafe-order-system.git
```

2. Заходим внутрь приложения и учтавливаем зависимости

```
poetry install --with dev
```

3. Создайте .env.prod
   Пример:

```
PYTHONPATH = src
DJANGO_ENV = production
SECRET_KEY = your_secret_key

DB_NAME = db
DB_USER = user
DB_PASSWORD = 12345678
DB_HOST = db

# POSTGRES
POSTGRES_DB = db
POSTGRES_USER = user
POSTGRES_PASSWORD = 12345678
```

4. Запустите приложение

```
poetry run poe up_prod
```

### Инструкция запуска dev среды

```
poetry install --with dev
```

Поднять инфраструктуру

```
poetry poe up
```

Запустить приложение

```
poetry run poe runserver
```