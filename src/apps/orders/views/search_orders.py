from django.contrib.postgres.search import (
    SearchVector,
    SearchRank,
    SearchQuery,
)
from django.db.models import Case, When, Value
from django.views.generic import ListView

from apps.orders.forms import OrderUpdateForm
from apps.orders.models import Order
from config.settings import ORDER_PAGINATE_BY


class OrderSearchView(ListView):
    template_name = "orders/list.html"
    extra_context = {
        "selected": "orders",
        "update_status_form": OrderUpdateForm,
    }
    context_object_name = "orders"
    paginate_by = ORDER_PAGINATE_BY

    def get_queryset(self):
        query = self.request.GET.get("query")

        if not query:
            return Order.objects.all()

        search_query = SearchQuery(query)
        return (
            Order.objects.annotate(  # TODO: GIN index
                status_text=Case(
                    *[
                        When(status=db_value, then=Value(label))
                        for db_value, label in Order.Status.choices
                    ],
                    default=Value(""),
                ),
                rank=SearchRank(
                    SearchVector("id", "status_text"),
                    search_query,
                ),
            )
            .filter(rank__gt=0.001)
            .order_by("-rank")
        )
