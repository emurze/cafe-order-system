import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from apps.orders.models import Order
from apps.orders.tests.api_views.conftest import make_order, get_order


@pytest.mark.django_db
def test_can_create_order(api_client: APIClient) -> None:
    # act
    response = make_order(api_client)

    # assert
    assert response.status_code == status.HTTP_201_CREATED

    order = Order.objects.first()
    response = get_order(api_client, order.id)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_cannot_create_order_when_order_is_empty(
        api_client: APIClient,
        faker: Faker,
) -> None:
    # act
    url = reverse("order-list")
    data = {"table_number": faker.random_int(1, 5), "items": []}
    response = api_client.post(url, data=data)

    # assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
