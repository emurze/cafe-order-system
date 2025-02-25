import pytest
from model_bakery import baker

from apps.orders import services
from apps.orders.models import Order


@pytest.mark.django_db
def test_can_search_orders() -> None:
    # arrange
    order = baker.make("Order")
    baker.make("Order")

    # act
    queryset = services.search_orders(Order.objects.all(), query=f"{order.id}")

    # assert
    assert queryset.count() == 1


@pytest.mark.django_db
def test_can_search_orders_when_query_is_empty() -> None:
    # arrange
    baker.make("Order")
    baker.make("Order")

    # act
    queryset = services.search_orders(Order.objects.all(), query="")

    # assert
    assert queryset.count() == 2
