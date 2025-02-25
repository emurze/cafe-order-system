from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.db.models import Case, When, Value, QuerySet

from apps.orders.models import Order


def search_orders(queryset: QuerySet, query: str) -> QuerySet:
    if not query:
        return queryset

    search_query = SearchQuery(query)
    return (
        queryset.annotate(
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
