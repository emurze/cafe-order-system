from rest_framework import serializers

from apps.orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for displaying details of an OrderItem."""

    class Meta:
        model = OrderItem
        fields = (
            "dish",
            "price",
            "quantity",
        )


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for displaying details of an Order, including order items."""

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "table_number",
            "total_price",
            "status",
            "created_at",
            "paid_at",
            "items",
        )


class OrderItemCreateSerializer(serializers.ModelSerializer):
    """Serializer for validating data for an OrderItem."""

    class Meta:
        model = OrderItem
        fields = ("dish", "price", "quantity")


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for validating data for creating an Order."""

    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "table_number",
            "items",
        )


class OrderUpdateSerializer(serializers.ModelSerializer):
    """Serializer for validating data for updating the status of an Order"""

    class Meta:
        model = Order
        fields = ("status",)


class OrderShiftRevenueSerializer(serializers.Serializer):
    """
    Serializer for validating the start and end times
    for calculating shift revenue.
    """

    start_time = serializers.TimeField(
        label="Начало смены (HH:MM)",
        input_formats=["%H:%M"],
    )
    end_time = serializers.TimeField(
        label="Конец смены (HH:MM)",
        input_formats=["%H:%M"],
    )
