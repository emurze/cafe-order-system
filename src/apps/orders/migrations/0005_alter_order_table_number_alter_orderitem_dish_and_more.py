# Generated by Django 5.1.6 on 2025-02-23 10:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "orders",
            "0004_alter_order_options_alter_order_table_number_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="table_number",
            field=models.PositiveIntegerField(
                unique=True, verbose_name="Номер стола"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="dish",
            field=models.CharField(
                max_length=256, verbose_name="Название блюда"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[
                    django.core.validators.MinValueValidator(
                        0.01, message="Стоимость должна быть не менее 0.01."
                    ),
                    django.core.validators.MaxValueValidator(
                        1000000, message="Цена не может превышать 1000000."
                    ),
                ],
                verbose_name="Cтоймость",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, message="Количество должно быть не менее 1."
                    ),
                    django.core.validators.MaxValueValidator(
                        1000, message="Количество не может превышать 1000."
                    ),
                ],
                verbose_name="Количество",
            ),
        ),
    ]
