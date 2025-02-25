from rest_framework import serializers

from apps.orders.models import Order, OrderItem


# GET


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "dish",
            "price",
            "quantity",
        )


class OrderSerializer(serializers.ModelSerializer):
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


# CREATE


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("dish", "price", "quantity")


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "table_number",
            "items",
        )


# UPDATE


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("status",)


# SHIFT REVENUE


class OrderShiftRevenueSerializer(serializers.Serializer):
    start_time = serializers.TimeField(
        label="Начало смены (HH:MM)",
        input_formats=["%H:%M"],
    )
    end_time = serializers.TimeField(
        label="Конец смены (HH:MM)",
        input_formats=["%H:%M"],
    )
