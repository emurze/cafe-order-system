import pytest
from faker import Faker

from apps.orders import services
from apps.orders.exceptions import OrderNotFoundException
from apps.orders.models import Order
from apps.orders.tests.services.conftest import make_order


@pytest.mark.django_db
def test_can_delete_order() -> None:
    # arrange
    order_id = make_order()

    # act
    services.delete_order(order_id)

    # assert
    assert not Order.objects.exists()


@pytest.mark.django_db
def test_cannot_delete_order_not_found_error(faker: Faker) -> None:
    # act / assert
    with pytest.raises(OrderNotFoundException):
        services.delete_order(faker.random_int(1, 10))
