import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker
from model_bakery import baker
from rest_framework import status

from apps.orders.models import Order


@pytest.mark.django_db
def test_can_delete_order(client: Client) -> None:
    # arrange
    order = baker.make("Order")

    # act
    url = reverse("orders:delete", args=(order.id,))
    response = client.delete(url)

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert not Order.objects.exists()


@pytest.mark.django_db
def test_cannot_delete_order_error_404(client: Client, faker: Faker) -> None:
    # act
    url = reverse("orders:delete", args=(faker.random_int(1, 10),))
    response = client.delete(url)

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
