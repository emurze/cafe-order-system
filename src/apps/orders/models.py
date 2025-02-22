from django.db import models


class Order(models.Model):
    class Status(models.TextChoices):  # Статусы на русском?
        """# (статус заказа: “в ожидании”, “готово”, “оплачено”)"""

        PENDING = "PG", "в ожидании"
        READY = "RD", "готово"
        PAID = "PD", "оплачено"

    id = models.BigAutoField(primary_key=True)
    table_number = models.PositiveSmallIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 1. price, currency !!! MUST HAVE

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
    dish = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(
        to="Order",
        related_name="items",
        on_delete=models.CASCADE,
    )
    # 2. quantity !!! MUST HAVE
