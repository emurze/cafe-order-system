# Generated by Django 5.1.6 on 2025-02-26 02:06

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0010_order_orders_orde_status_079368_idx_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(
                blank=True, null=True
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="status_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name="order",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="orders_orde_search__5b7dab_gin"
            ),
        ),
    ]
