from django.contrib.postgres.search import (
    SearchVector,
    SearchRank,
    SearchQuery,
)
from django.db.models import Case, When, Value
from django.views.generic import ListView

from apps.orders.models import Order


class OrderSearchView(ListView):
    template_name = "orders/list.html"
    extra_context = {"selected": "orders"}
    context_object_name = "orders"
    paginate_by = 18

    def get_queryset(self):
        query = self.request.GET.get("query")

        if not query:
            return Order.objects.all()  # TODO

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
