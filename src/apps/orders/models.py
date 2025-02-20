from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from apps.dishes.models import Dish


class Order(models.Model):
    class Status(models.TextChoices):  # Статусы на русском?
        """# (статус заказа: “в ожидании”, “готово”, “оплачено”)"""

        PENDING = "PG", "Pending"
        READY = "RD", "Ready"
        PAID = "PD", "Paid"

    id = models.BigAutoField(primary_key=True)
    table_numbers = models.PositiveSmallIntegerField()
    items = models.ForeignKey(
        to="OrderItem",
        related_name="orders",
        on_delete=models.CASCADE,
    )
    # общая стоимость заказа, вычисляется автоматическиs
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING,
    )

    # class Meta


class OrderItem(models.Model):
    """Заказанное блюдо с ценой"""

    id = models.BigAutoField(primary_key=True)
    dish = models.ForeignKey(  # TODO
        "dishes.Dish",
        related_name="order_items",
        on_delete=models.SET_NULL,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
