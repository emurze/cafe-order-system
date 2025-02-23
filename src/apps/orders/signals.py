from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order


@receiver(pre_save, sender=Order)
def update_order_total_price(sender, instance, **__):
    if instance.pk:
        instance.total_price = instance.get_total_price()
