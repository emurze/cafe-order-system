from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

ALLOWED_HOSTS = [
    "192.168.0.104",
    "127.0.0.1",
    "localhost",
    "cafe-order-system",
    "0.0.0.0",
    "127.0.0.1",
]
