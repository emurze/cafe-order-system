from django.db.models import Prefetch

from apps.orders.models import Order, OrderItem


class OrderLongQueryMixin:
    """Mixin for handling long queries related to order data."""

    def get_queryset(self):
        return Order.objects.only(
            "id",
            "table_number",
            "total_price",
            "status",
        ).prefetch_related(
            Prefetch(
                "items",
                OrderItem.objects.only(
                    "id",
                    "dish",
                    "price",
                    "quantity",
                    "order_id",
                ),
            )
        )


class OrderShortQueryMixin(OrderLongQueryMixin):
    """
    Mixin for handling short queries related to order data.
    For now, it functions identically to the long query mixin.
    """
