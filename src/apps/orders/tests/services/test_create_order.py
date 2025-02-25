import pytest

from apps.orders.models import Order
from apps.orders.tests.services.conftest import make_order


@pytest.mark.django_db
def test_can_create_order() -> None:
    # act
    make_order()

    # assert
    assert Order.objects.exists()
