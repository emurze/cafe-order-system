from django.db import transaction

from apps.orders.models import Order, OrderItem


def create_order(order_dto: dict, item_list_dto: list[dict]) -> int:
    """Creates a new order and associated order items."""
    with transaction.atomic():
        order = Order(**order_dto, total_price=0)
        order.save()

        for item_data in item_list_dto:
            order_item = OrderItem(order=order, **item_data)
            order_item.save()

        order.save()
        order_id = order.id

    return order_id
