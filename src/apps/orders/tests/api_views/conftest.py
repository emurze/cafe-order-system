from typing import Any

from django.urls import reverse
from faker import Faker
from rest_framework.test import APIClient


def make_order(api_client: APIClient) -> Any:
    faker = Faker()
    url = reverse("order-list")
    return api_client.post(
        url,
        data={
            "table_number": faker.random_int(1, 5),
            "items": [
                {
                    "dish": faker.word(),
                    "price": faker.random_int(),
                    "quantity": 2,
                }
            ],
        },
        format="json",
    )


def get_order(api_client: APIClient, order_id: int) -> Any:
    url = reverse("order-detail", args=(order_id,))
    return api_client.get(url)
