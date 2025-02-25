from datetime import datetime

import pytest
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from model_bakery import baker
from rest_framework import status

from apps.orders.models import Order


def _make_order(start_datetime: datetime, timedelta_hours: int) -> Order:
    faker = Faker()
    return baker.make(
        "Order",
        status=Order.Status.PAID,
        total_price=faker.random_int(1, 100),
        paid_at=start_datetime + timezone.timedelta(hours=timedelta_hours),
    )


@pytest.mark.django_db
def test_can_get_shift_revenue(client: Client) -> None:
    # arrange
    today = timezone.now().date()
    start_time = timezone.datetime.strptime("05:00", "%H:%M").time()
    end_time = timezone.datetime.strptime("12:00", "%H:%M").time()
    start_datetime = timezone.make_aware(
        timezone.datetime.combine(today, start_time)
    )

    order1 = _make_order(start_datetime, timedelta_hours=1)
    order2 = _make_order(start_datetime, timedelta_hours=2)

    # act
    url = reverse("orders:shift_revenue")
    response = client.get(
        url,
        {
            "start_time": start_time.strftime("%H:%M"),
            "end_time": end_time.strftime("%H:%M"),
        },
    )
    context = response.context

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert context["revenue"] == order1.total_price + order2.total_price
    assert context["total_orders"] == 2
