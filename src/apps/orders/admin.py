from django.contrib import admin

from apps.orders.models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Admin class for managing order items"""

    list_display = (
        "dish",
        "price",
        "quantity",
    )


class OrderItemInline(admin.TabularInline):
    """Inline form for displaying and editing order items."""

    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin class for managing orders."""

    list_display = (
        "id",
        "table_number",
        "total_price",
        "status",
    )
    inlines = (OrderItemInline,)
