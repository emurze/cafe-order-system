from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.base.signals import generate_unique_slug
from apps.dishes.models import Dish


@receiver(pre_save, sender=Dish)
def generate_slug(sender, instance, **__) -> None:
    if instance.pk:
        old_instance = Dish.objects.get(pk=instance.pk)
        if old_instance.title != instance.title:  # Title has changed
            instance.slug = generate_unique_slug(sender, instance.title)
    else:
        instance.slug = generate_unique_slug(sender, instance.title)
