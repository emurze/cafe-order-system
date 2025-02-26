from django.contrib.postgres.search import SearchVector
from django.db.models import Case, When, Value
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from config.settings import SEARCH_QUERY_CONFIG
from .models import Order


@receiver(pre_save, sender=Order)
def update_order_total_price(
    sender: type[Order],
    instance: Order,
    **__,
) -> None:
    """Ensures the total price is consistent with the order's items."""
    if instance.pk:
        instance.total_price = instance.get_total_price()


@receiver(pre_save, sender=Order)
def set_paid_at(sender: type[Order], instance: Order, **__) -> None:
    """Sets the paid_at field when the order status is PAID."""
    if instance.status == sender.Status.PAID and instance.pk:
        instance.paid_at = timezone.now()


@receiver(post_save, sender=Order)
def update_search_vector(sender, instance, **__) -> None:
    """Updates search-related fields for GIN indexing."""
    order = sender.objects.filter(pk=instance.pk)
    order.update(
        status_text=Case(
            *[
                When(status=db_value, then=Value(label))
                for db_value, label in Order.Status.choices
            ],
            default=Value(""),
        )
    )
    order.update(
        search_vector=SearchVector(
            "id",
            "status_text",
            config=SEARCH_QUERY_CONFIG,
        )
    )
