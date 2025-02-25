from django.db import transaction

from apps.orders.exceptions import OrderNotFoundException
from apps.orders.models import Order


def delete_order(pk: int) -> None:
    with transaction.atomic():
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise OrderNotFoundException()

        order.delete()
