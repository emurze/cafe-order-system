from decimal import Decimal
from typing import TYPE_CHECKING, Optional

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from faker import Faker
from model_bakery import baker

if TYPE_CHECKING:
    from apps.orders.models import Order, OrderItem


def make_order_item(
        order: Optional["Order"] = None,
        price: Decimal | None = None,
        quantity: int | None = None,
) -> "OrderItem":
    faker = Faker()
    return baker.make(
        "OrderItem",
        order=order if order is not None else baker.make("Order"),
        dish=faker.word(),
        price=price if price is not None else Decimal(faker.random_int(1, 10)),
        quantity=(
            quantity if quantity is not None else faker.random_int(1, 10)
        ),
    )


class TestOrder:
    @pytest.mark.django_db
    def test_can_calculate_total_price(self) -> None:
        # arrange
        order = baker.make("Order")
        item1 = make_order_item(order=order)
        item2 = make_order_item(order=order)

        # act / assert
        assert (
                order.get_total_price()
                == item1.price * item1.quantity + item2.price * item2.quantity
        )

    @pytest.mark.django_db
    def test_cannot_create_two_orders_with_same_table_number(
            self,
            faker: Faker,
    ) -> None:
        # arrange
        table_number = faker.random_int(1, 5)
        baker.make("Order", table_number=table_number)

        # act / assert
        with pytest.raises(IntegrityError):
            baker.make("Order", table_number=table_number)


class TestOrderItem:
    @pytest.mark.django_db
    @pytest.mark.parametrize("price", [Decimal(0), Decimal(1_000_001)])
    def test_cannot_create_order_item_when_price_is_invalid(
            self, price: Decimal
    ) -> None:
        # arrange
        order_item = make_order_item(price=price)

        # act / assert
        with pytest.raises(ValidationError):
            order_item.full_clean()

    @pytest.mark.django_db
    @pytest.mark.parametrize("quantity", [0, 1001])
    def test_cannot_create_order_item_when_quantity_is_invalid(
            self, quantity: int
    ) -> None:
        # arrange
        order_item = make_order_item(quantity=quantity)

        # act / assert
        with pytest.raises(ValidationError):
            order_item.full_clean()
