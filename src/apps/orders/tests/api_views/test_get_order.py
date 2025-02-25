import pytest
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from apps.orders.models import Order
from apps.orders.tests.api_views.conftest import make_order, get_order


@pytest.mark.django_db
def test_can_get_order(api_client: APIClient) -> None:
    # arrange
    make_order(api_client)

    # act
    order = Order.objects.first()
    response = get_order(api_client, order.id)

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == order.id


@pytest.mark.django_db
def test_cannot_get_order_error_404(
        api_client: APIClient,
        faker: Faker,
) -> None:
    # act
    response = get_order(api_client, faker.random_int(1, 10))

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
