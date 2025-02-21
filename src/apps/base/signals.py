import random
import string

from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


def generate_unique_slug(model_class: models.Model, obj: str) -> str:
    """Generate a unique slug by appending a random string if needed"""
    ascii_title = unidecode(obj)
    base_slug = slugify(ascii_title)
    slug = base_slug

    while model_class.objects.filter(slug=slug).exists():
        random_string = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=6)
        )
        slug = f"{base_slug}-{random_string}"

    return slug
