import pytest
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from apps.orders.models import Order


@pytest.mark.django_db
def test_can_get_shift_revenue(api_client: APIClient, faker: Faker) -> None:
    # arrange
    today = timezone.now().date()
    start_time = timezone.datetime.strptime("05:00", "%H:%M").time()
    end_time = timezone.datetime.strptime("12:00", "%H:%M").time()
    start_datetime = timezone.make_aware(
        timezone.datetime.combine(today, start_time)
    )

    baker.make(
        "Order",
        status=Order.Status.PAID,
        total_price=faker.random_int(1, 100),
        paid_at=start_datetime + timezone.timedelta(hours=15),
    )
    order2 = baker.make(
        "Order",
        status=Order.Status.PAID,
        total_price=faker.random_int(1, 100),
        paid_at=start_datetime + timezone.timedelta(hours=3),
    )

    # act
    url = reverse("order-shift-revenue")
    response = api_client.get(
        f"{url}?start_time={start_time.strftime("%H:%M")}&"
        f"end_time={end_time.strftime("%H:%M")}"
    )

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["total_revenue"] == order2.total_price


@pytest.mark.django_db
def test_cannot_get_shift_revenue_when_query_is_invalid(
    api_client: APIClient,
) -> None:
    # act
    url = reverse("order-shift-revenue")
    response = api_client.get(f"{url}?start_time=...&end_time=...")

    # assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
