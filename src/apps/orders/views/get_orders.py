from django.views.generic import ListView

from apps.orders.forms import OrderUpdateForm
from apps.orders.mixins import OrderLongQueryMixin
from config.settings import ORDER_PAGINATE_BY


class OrderListView(OrderLongQueryMixin, ListView):
    """View to display a list of orders with pagination."""

    context_object_name = "orders"
    template_name = "orders/list.html"
    extra_context = {
        "selected": "orders",
        "update_status_form": OrderUpdateForm,
    }
    paginate_by = ORDER_PAGINATE_BY
