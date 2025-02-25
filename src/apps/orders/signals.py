from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Order


@receiver(pre_save, sender=Order)
def update_order_total_price(
        sender: type[Order],
        instance: Order,
        **__,
) -> None:
    if instance.pk:
        instance.total_price = instance.get_total_price()


@receiver(pre_save, sender=Order)
def set_paid_at(sender: type[Order], instance: Order, **__) -> None:
    if instance.status == sender.Status.PAID and instance.pk:
        instance.paid_at = timezone.now()
