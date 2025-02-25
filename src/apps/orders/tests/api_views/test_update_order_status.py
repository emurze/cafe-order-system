import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from apps.orders.models import Order
from apps.orders.tests.api_views.conftest import make_order, get_order


@pytest.mark.django_db
def test_can_update_order_status(api_client: APIClient) -> None:
    # arrange
    make_order(api_client)
    order = Order.objects.first()

    # act
    url = reverse("order-detail", kwargs={"pk": order.pk})
    response = api_client.patch(url, data={"status": order.Status.READY.value})

    # assert
    assert response.status_code == status.HTTP_200_OK

    _response = get_order(api_client, order.pk)
    assert _response.data["status"] == order.Status.READY.value


@pytest.mark.django_db
def test_update_order_status_nonexistent_order(
        api_client: APIClient,
        faker: Faker,
) -> None:
    # act
    url = reverse("order-detail", kwargs={"pk": faker.random_int(1, 10)})
    response = api_client.patch(url, data={"status": Order.Status.READY.value})

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
