from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import DecimalField
from django.urls import reverse


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "1", "в ожидании"
        READY = "2", "готово"
        PAID = "3", "оплачено"

    id = models.BigAutoField(primary_key=True)
    table_number = models.PositiveIntegerField("Номер стола")
    total_price = DecimalField(
        "Полная стоймость",
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
        ],
    )
    status = models.CharField(
        "Статус",
        max_length=1,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:  # TODO
        ordering = (
            "status",
            "-created_at",
        )
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def get_total_price(self) -> Decimal:
        return Decimal(sum(item.get_price() for item in self.items.all()))

    def get_absolute_url(self) -> str:
        return reverse("orders:detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{type(self).__name__}(id={self.id!r})"


class OrderItem(models.Model):
    """Заказанное блюдо с ценой"""

    id = models.BigAutoField(primary_key=True)
    dish = models.CharField("Название блюда", max_length=256)
    price = DecimalField(
        "Cтоймость",
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(
                0.01, message="Стоимость должна быть не менее 0.01."
            ),
            MaxValueValidator(
                1_000_000, message="Цена не может превышать 1000000."
            ),
        ],
    )
    order = models.ForeignKey(
        to="Order",
        related_name="items",
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField(
        "Количество",
        validators=[
            MinValueValidator(1, message="Количество должно быть не менее 1."),
            MaxValueValidator(
                1000, message="Количество не может превышать 1000."
            ),
        ],
    )

    def get_price(self) -> Decimal:
        return self.price * self.quantity

    def __str__(self) -> str:
        return (
            f"{type(self).__name__}(dish={self.dish!r}, "
            f"price={self.price!r}, quantity={self.quantity!r})"
        )
