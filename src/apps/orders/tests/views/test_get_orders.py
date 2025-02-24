import pytest
from django.test import Client
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
def test_can_get_orders(client: Client) -> None:
    # arrange
    baker.make("Order")
    baker.make("Order")

    # act
    url = reverse("orders:list")
    response = client.get(url)
    queryset = response.context["orders"]

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert queryset.count() == 2
