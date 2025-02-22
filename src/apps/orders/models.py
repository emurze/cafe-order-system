from django.db import models
from djmoney.models.fields import MoneyField


class Order(models.Model):
    class Status(models.TextChoices):  # Статусы на русском?
        """# (статус заказа: “в ожидании”, “готово”, “оплачено”)"""

        PENDING = "PG", "в ожидании"
        READY = "RD", "готово"
        PAID = "PD", "оплачено"

    id = models.BigAutoField(primary_key=True)
    table_number = models.PositiveSmallIntegerField("Номер столика")
    total_price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency="BYN",
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # ???

    class Meta:
        ordering = ("-created_at",)  # TODO:

    # общая стоимость заказа, вычисляется автоматическиs ЗДЕСЬ

    def __str__(self) -> str:
        return f"{type(self).__name__}(title={self.id!r})"


class OrderItem(models.Model):
    """Заказанное блюдо с ценой"""

    id = models.BigAutoField(primary_key=True)
    dish = models.CharField("Название блюда", max_length=256)
    price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency="BYN",
    )
    order = models.ForeignKey(
        to="Order",
        related_name="items",
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField("Количество")
