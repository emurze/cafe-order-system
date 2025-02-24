import pytest
from django.test import Client
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
def test_can_search_orders(client: Client) -> None:
    # arrange
    order = baker.make("Order")
    baker.make("Order")

    # act
    url = reverse("orders:search")
    response = client.get(f"{url}?query={order.id}")
    queryset = response.context["orders"]

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert queryset.count() == 1


@pytest.mark.django_db
def test_can_search_orders_when_query_is_empty(client: Client) -> None:
    # arrange
    baker.make("Order")
    baker.make("Order")

    # act
    url = reverse("orders:search")
    response = client.get(f"{url}")
    queryset = response.context["orders"]

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert queryset.count() == 2
