import pytest
from django.shortcuts import resolve_url
from django.test import Client
from faker import Faker
from rest_framework import status

from apps.orders.forms import ORDER_CANNOT_BE_EMPTY_ERROR
from apps.orders.models import Order, OrderItem

ONE_FORM_CONF = {
    "form-INITIAL_FORMS": [0],
    "form-MAX_NUM_FORMS": [1000],
    "form-MIN_NUM_FORMS": [0],
    "form-TOTAL_FORMS": [1],
}


@pytest.mark.django_db
def test_can_create_order(client: Client, faker: Faker) -> None:
    # act
    url = resolve_url("orders:create")
    response = client.post(
        url,
        data={
            "form-0-dish": [faker.word()],
            "form-0-price": [faker.random_int(min=1, max=10)],
            "form-0-quantity": [faker.random_int(min=1, max=10)],
            "table_number": [faker.random_int(min=1, max=10)],
            **ONE_FORM_CONF,
        },
    )

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert Order.objects.count() == 1
    assert OrderItem.objects.count() == 1


@pytest.mark.django_db
def test_cannot_create_order_when_order_is_empty(
        client: Client,
        faker: Faker,
) -> None:
    # act
    url = resolve_url("orders:create")
    response = client.post(
        url,
        data={
            "form-0-dish": [""],
            "form-0-price": [""],
            "form-0-quantity": [""],
            "table_number": [faker.random_int(min=1, max=10)],
            **ONE_FORM_CONF,
        },
    )

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert ORDER_CANNOT_BE_EMPTY_ERROR in response.content.decode()
    assert not Order.objects.exists()
