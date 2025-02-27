# Generated by Django 5.1.6 on 2025-02-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0009_alter_order_options_order_paid_at"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["status", "-created_at"],
                name="orders_orde_status_079368_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["status", "paid_at"],
                name="orders_orde_status_e8f3be_idx",
            ),
        ),
    ]
