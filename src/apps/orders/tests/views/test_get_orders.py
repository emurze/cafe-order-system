import pytest
from django.test import Client
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
def test_can_get_orders(client: Client) -> None:
    # arrange
    order = baker.make("Order")
    order2 = baker.make("Order")

    # act
    url = reverse("orders:list")
    response = client.get(url)

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert str(order.id) in response.content.decode("utf-8")
    assert str(order2.id) in response.content.decode("utf-8")
