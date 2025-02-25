import pytest
from faker import Faker

from apps.orders import services
from apps.orders.exceptions import OrderNotFoundException
from apps.orders.models import Order
from apps.orders.tests.services.conftest import make_order


@pytest.mark.django_db
def test_can_update_order_status() -> None:
    # arrange
    order_id = make_order()

    # act
    services.update_order_status(order_id, Order.Status.READY)

    # assert
    order = Order.objects.get(pk=order_id)
    assert order.status == Order.Status.READY


@pytest.mark.django_db
def test_cannot_update_order_status_not_found_error(faker: Faker) -> None:
    # act / assert
    with pytest.raises(OrderNotFoundException):
        services.update_order_status(
            faker.random_int(1, 10),
            Order.Status.READY,
        )
