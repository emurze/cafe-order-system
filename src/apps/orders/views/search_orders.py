from django.db.models import QuerySet
from django.views.generic import ListView

from apps.orders import services
from apps.orders.forms import OrderUpdateForm
from apps.orders.mixins import OrderLongQueryMixin
from config.settings import ORDER_PAGINATE_BY


class OrderSearchView(OrderLongQueryMixin, ListView):
    """View for searching orders based on a query parameter."""

    template_name = "orders/list.html"
    extra_context = {
        "selected": "orders",
        "update_status_form": OrderUpdateForm,
    }
    context_object_name = "orders"
    paginate_by = ORDER_PAGINATE_BY

    def get_queryset(self) -> QuerySet:
        query = self.request.GET.get("query")
        queryset = super().get_queryset()
        return services.search_orders(queryset, query)
