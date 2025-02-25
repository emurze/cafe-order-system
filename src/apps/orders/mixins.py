from django.db.models import Prefetch

from apps.orders.models import Order, OrderItem


class OrderLongQueryMixin:
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
    """OrderShortQueryMixin uses The same fields"""  # TODO
