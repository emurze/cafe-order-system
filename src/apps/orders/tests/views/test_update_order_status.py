import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker
from model_bakery import baker
from rest_framework import status

from apps.orders.models import Order


@pytest.mark.django_db
def test_can_update_order_status(client: Client) -> None:
    # arrange
    order = baker.make("Order")

    # act
    url = reverse("orders:update", args=(order.id,))
    response = client.post(url, data={"status": order.Status.READY})
    order.refresh_from_db()

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse("orders:list")
    assert order.status == order.Status.READY


@pytest.mark.django_db
def test_update_order_and_redirect_to_detail(client: Client) -> None:
    # arrange
    order = baker.make("Order")

    # act
    url = reverse("orders:update", args=(order.id,))
    response = client.post(
        url,
        data={
            "status": order.Status.READY,
            "redirect_to_detail": True,
        },
    )
    order.refresh_from_db()

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse("orders:detail", args=(order.id,))
    assert order.status == order.Status.READY


@pytest.mark.django_db
def test_cannot_update_order_invalid_form(
        client: Client,
        faker: Faker,
) -> None:
    # arrange
    order = baker.make("Order")

    # act
    url = reverse("orders:update", args=(faker.random_int(1, 5),))
    response = client.post(url, data={"status": "invalid_status"})
    order.refresh_from_db()

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse("orders:list")
    assert order.status == order.Status.PENDING


@pytest.mark.django_db
def test_update_order_status_nonexistent_order(
        client: Client,
        faker: Faker,
) -> None:
    # act
    url = reverse("orders:update", args=(faker.random_int(1, 5),))
    response = client.post(url, data={"status": Order.Status.READY})

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
