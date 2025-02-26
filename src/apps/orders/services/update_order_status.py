from django.db import transaction

from apps.orders.exceptions import OrderNotFoundException
from apps.orders.models import Order


def update_order_status(pk: int, status: Order.Status) -> None:
    """Updates the status of an order."""
    with transaction.atomic():
        try:
            order = Order.objects.select_for_update().get(pk=pk)
        except Order.DoesNotExist:
            raise OrderNotFoundException()

        order.status = status
        order.save()
