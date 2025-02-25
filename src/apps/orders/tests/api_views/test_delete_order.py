import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from apps.orders.models import Order
from apps.orders.tests.api_views.conftest import make_order, get_order


@pytest.mark.django_db
def test_can_delete_order(api_client: APIClient) -> None:
    # arrange
    make_order(api_client)
    order = Order.objects.first()

    # act
    url = reverse("order-detail", args=(order.id,))
    response = api_client.delete(url)

    # assert
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response = get_order(api_client, order.id)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_cannot_delete_order_error_404(
        api_client: APIClient,
        faker: Faker,
) -> None:
    # act
    url = reverse("order-detail", args=(faker.random_int(1, 5),))
    response = api_client.delete(url)

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
