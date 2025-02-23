from django.contrib import admin

from apps.orders.models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "dish",
        "price",
        "quantity",
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "table_number",
        "total_price",
        "status",
    )
    inlines = (OrderItemInline,)
