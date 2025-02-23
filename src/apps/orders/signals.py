from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def update_order_total_price(sender, instance, **__):
    instance.total_price = instance.get_total_price()
