# Cистема управления заказами в кафе

https://docs.google.com/document/d/1-VJZRZhaWjtcqN-edMS2EKp621eMHqho9hPaZWSe8Og/edit?tab=t.0#heading=h.c8vqchg2yga1

Убедитесь, что у вас установлен докер.

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

### Инструкция запуска прода

```
poetry install
```

Запустить продакшион

```
poetry run poe run_prod
```
