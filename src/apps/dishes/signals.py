import random
import string

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from apps.dishes.models import Dish


def generate_unique_slug(model_class: models.Model, base_slug: str):
    """Generate a unique slug by appending a random string if needed"""
    slug = base_slug

    while model_class.objects.filter(slug=slug).exists():
        random_string = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=6)
        )
        slug = f"{base_slug}-{random_string}"

    return slug


@receiver(pre_save, sender=Dish)
def generate_slug(sender, instance, **__) -> None:
    if not instance.slug:
        base_slug = slugify(instance.title)
        instance.slug = generate_unique_slug(sender, base_slug)
