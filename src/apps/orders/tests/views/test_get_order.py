import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
def test_can_get_order(client: Client) -> None:
    # arrange
    order = baker.make("Order")

    # act
    url = reverse("orders:detail", args=(order.id,))
    response = client.get(url)

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert str(order.id) in response.content.decode("utf-8")


@pytest.mark.django_db
def test_cannot_get_order_error_404(client: Client, faker: Faker) -> None:
    # act
    url = reverse("orders:detail", args=(faker.random_int(1, 10),))
    response = client.get(url)

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
