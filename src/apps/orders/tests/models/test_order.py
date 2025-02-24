from decimal import Decimal
from typing import TYPE_CHECKING, Optional

import pytest
from django.core.exceptions import ValidationError
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
    @staticmethod
    def _get_total_price(items: list["OrderItem"]) -> Decimal:
        return Decimal(sum(item.price * item.quantity for item in items))

    @pytest.mark.django_db
    def test_can_calculate_total_price(self) -> None:
        # arrange
        order = baker.make("Order")
        item1 = make_order_item(order=order)
        item2 = make_order_item(order=order)

        # act
        order.save()

        # assert
        assert order.total_price == self._get_total_price([item1, item2])

    @pytest.mark.django_db
    def test_can_recalculate_total_price_after_save(self) -> None:
        # arrange
        order = baker.make("Order")
        item1 = make_order_item(order=order)
        item2 = make_order_item(order=order)
        order.save()

        # act
        item3 = make_order_item(order=order)
        order.save()

        # act / assert
        assert order.total_price == self._get_total_price(
            [item1, item2, item3]
        )


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
