# Система управления заказами в кафе

Перед установкой убедитесь, что у вас установлен **Docker** и **Poetry** для
управления зависимостями.

### Инструкция по установке

#### 1. Скачайте репозиторий с GitHub

Для начала, клонируйте репозиторий на вашу машину с помощью Git:

```bash
git clone git@github.com:emurze/cafe-order-system.git
```

Перейдите в папку с проектом:

```bash
cd cafe-order-system
```

#### 2. Установите зависимости с помощью Poetry

Убедитесь, что у вас установлен **Poetry**. Если нет, установите его, следуя
инструкциям на официальном сайте
Poetry: https://python-poetry.org/docs/#installation.

Затем установите все зависимости проекта, включая зависимости для разработки:

```bash
poetry install --with dev
```

#### 3. Настройте файл окружения

Создайте файл конфигурации `.env.prod` для настройки переменных окружения.
Пример:

```bash
touch .env.prod
```

Пример содержимого файла `.env.prod`:

```ini
# Общие настройки
PYTHONPATH = src
DJANGO_ENV = production
SECRET_KEY = secret_key  # Вставьте сюда ваш собственный секретный ключ

# Настройки базы данных
DB_NAME = db
DB_USER = user
DB_PASSWORD = 12345678
DB_HOST = db

# Настройки PostgreSQL
POSTGRES_DB = db
POSTGRES_USER = user
POSTGRES_PASSWORD = 12345678
```

#### 4. Запуск приложения в продакшн-режиме

Для запуска приложения в продакшн-режиме используйте следующую команду:

```bash
poetry run poe up_prod
```
Эта команда инициирует выполнение ```docker compose up```, запустив все необходимые контейнеры. 
После успешного старта приложение будет доступно по адресу: http://0.0.0.0:80.

#### 5. В случае проблем

Если вы столкнулись с проблемами при запуске, возможно, у вас уже есть
запущенные контейнеры Docker, которые могут конфликтовать с текущими. Для
остановки и удаления всех контейнеров используйте команду:

```bash
poetry run poe down_prod -v
```

Это удалит все контейнеры, созданные для продакшн-окружения, и вы сможете
заново запустить систему.

---

### Инструкция для запуска dev-среды

Если вы хотите работать в **разработческой среде**, следуйте инструкции ниже.

#### 1. Установка зависимостей

Установите все необходимые зависимости для разработки (аналогично шагу 2):

```bash
poetry install --with dev
```

#### 2. Запуск инфраструктуры для разработки

Для запуска приложения в режиме разработки и поднятия необходимых контейнеров
используйте команду:

```bash
poetry run poe up -d
```

#### 3. Применение миграций

Для применения миграций используйте команду:

```bash
poetry run poe migrate
```

#### 4. Запуск локального приложения

Для запуска локального приложения используйте команду:

```bash
poetry run poe runserver
```

Приложение будет доступно по
адресу [http://localhost:8000](http://localhost:8000) (если не указано иначе в
конфигурации).

---

### Полезные команды

- **Для остановки prod контейнеров**:

```bash
poetry run poe down_prod -v
```

- **Для остановки dev контейнеров**:

```bash
poetry run poe down -v
```
