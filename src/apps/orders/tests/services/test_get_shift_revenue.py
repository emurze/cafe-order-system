import datetime

import pytest
from django.utils import timezone
from faker import Faker
from model_bakery import baker

from apps.orders import services
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
def test_can_get_shift_revenue() -> None:
    # arrange
    today = timezone.now().date()
    start_time = timezone.datetime.strptime("05:00", "%H:%M").time()
    end_time = timezone.datetime.strptime("12:00", "%H:%M").time()
    start_datetime = timezone.make_aware(
        timezone.datetime.combine(today, start_time)
    )

    order1 = _make_order(start_datetime, timedelta_hours=2)
    order2 = _make_order(start_datetime, timedelta_hours=3)

    # act
    result = services.get_shift_revenue(start_time, end_time)

    # assert
    assert result["total_revenue"] == order1.total_price + order2.total_price
    assert result["total_orders"] == 2


@pytest.mark.django_db
def test_can_filter_unpaid_orders() -> None:
    # arrange
    today = timezone.now().date()
    start_time = timezone.datetime.strptime("05:00", "%H:%M").time()
    end_time = timezone.datetime.strptime("12:00", "%H:%M").time()
    start_datetime = timezone.make_aware(
        timezone.datetime.combine(today, start_time)
    )

    baker.make("Order")
    order = _make_order(start_datetime, timedelta_hours=2)

    # act
    result = services.get_shift_revenue(start_time, end_time)

    # assert
    assert result["total_revenue"] == order.total_price


@pytest.mark.django_db
def test_can_exclude_orders_outside_time_range() -> None:
    # arrange
    today = timezone.now().date()
    start_time = timezone.datetime.strptime("05:00", "%H:%M").time()
    end_time = timezone.datetime.strptime("12:00", "%H:%M").time()
    start_datetime = timezone.make_aware(
        timezone.datetime.combine(today, start_time)
    )

    _make_order(start_datetime, timedelta_hours=14)

    # act
    result = services.get_shift_revenue(start_time, end_time)

    # assert
    assert result["total_revenue"] == 0


@pytest.mark.django_db
def test_end_time_less_than_start_time_adjusts_to_next_day() -> None:
    # arrange
    today = timezone.now().date()
    start_time = timezone.datetime.strptime("22:00", "%H:%M").time()
    end_time = timezone.datetime.strptime("12:00", "%H:%M").time()
    start_datetime = timezone.make_aware(
        timezone.datetime.combine(today, start_time)
    )

    order = _make_order(start_datetime, timedelta_hours=5)
    _make_order(start_datetime, timedelta_hours=15)

    # act
    result = services.get_shift_revenue(start_time, end_time)

    # assert
    assert result["total_revenue"] == order.total_price
