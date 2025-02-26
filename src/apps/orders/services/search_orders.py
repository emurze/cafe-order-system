from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import QuerySet, F

from config.settings import SEARCH_QUERY_CONFIG


def search_orders(queryset: QuerySet, query: str) -> QuerySet:
    """Searches and ranks orders by relevance based on a query string."""

    if not query:
        return queryset

    search_query = SearchQuery(query, config=SEARCH_QUERY_CONFIG)
    q = (
        queryset.filter(search_vector=search_query)  # ✅ Uses GIN index
        .annotate(rank=SearchRank(F("search_vector"), search_query))
        .order_by("-rank")
    )
    return q
