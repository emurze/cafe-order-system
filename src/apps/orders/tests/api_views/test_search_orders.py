import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.orders.models import Order
from apps.orders.tests.api_views.conftest import make_order


@pytest.mark.django_db
def test_can_search_orders(api_client: APIClient) -> None:
    # arrange
    make_order(api_client)
    make_order(api_client)

    # act
    order = Order.objects.first()
    url = reverse("order-search-orders")
    response = api_client.get(f"{url}?query={order.id}")

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
