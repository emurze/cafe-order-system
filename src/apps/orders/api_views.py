from typing import Any

from django.db.models import Prefetch, QuerySet
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from apps.orders import services
from apps.orders.models import Order, OrderItem
from apps.orders.serializers import (
    OrderSerializer,
    OrderCreateSerializer,
    OrderUpdateSerializer,
    OrderShiftRevenueSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing orders in the system.

    Provides functionality for:
    - Creating an order.
    - Retrieving, listing, and updating order details.
    - Deleting orders.
    - Searching for orders based on a query string.
    - Retrieving shift revenue for a given time range.

    Actions:
        - `list`: Get a list of orders.
        - `retrieve`: Get details of a specific order.
        - `create`: Create a new order with associated items.
        - `update`: Update the status of an existing order.
        - `destroy`: Delete an existing order.
        - `search_orders`: Search for orders by a query string.
        - `shift_revenue`: Get total revenue and order count for a given shift.
    """

    serializer_class = OrderSerializer

    def get_queryset(self) -> QuerySet:
        """Returns the queryset of orders based on the current action."""
        if self.action in ("list", "retrieve", "search_orders"):
            return Order.objects.only(
                "id",
                "table_number",
                "total_price",
                "status",
                "created_at",
                "paid_at",
            ).prefetch_related(
                Prefetch(
                    "items",
                    queryset=OrderItem.objects.only(
                        "id",
                        "dish",
                        "price",
                        "quantity",
                        "order_id",
                    ),
                )
            )
        return Order.objects.all()

    def get_serializer_class(self) -> Any:
        """Returns the appropriate serializer class based on the action."""
        if self.action == "create":
            return OrderCreateSerializer
        elif self.action == "update":
            return OrderUpdateSerializer
        return super().get_serializer_class()

    def destroy(self, request, *args, **kwargs) -> Response:
        """Deletes an order and returns a 204 No Content response."""
        instance = self.get_object()
        services.delete_order(instance.id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer: OrderSerializer) -> None:
        """Creates a new order with associated items."""
        order_dto = {
            "table_number": serializer.validated_data["table_number"],
        }
        item_list_dto = serializer.validated_data["items"]
        services.create_order(order_dto, item_list_dto)

    def perform_update(self, serializer: OrderUpdateSerializer) -> None:
        """Updates an existing order's status."""
        _status = serializer.validated_data["status"]
        services.update_order_status(self.kwargs.get("pk"), _status)

    @action(detail=False, methods=["GET"], url_path="search")
    def search_orders(self, request: Request) -> Response:
        """Searches for orders based on a query provided in the request."""
        query = request.query_params.get("query")
        queryset = services.search_orders(self.get_queryset(), query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="shift-revenue")
    def shift_revenue(self, request: Request) -> Response:
        """
        Calculates and returns total revenue and order count for a shift.
        The shift is determined by the provided start and end time.
        """
        serializer = OrderShiftRevenueSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        start_time = serializer.validated_data["start_time"]
        end_time = serializer.validated_data["end_time"]
        result = services.get_shift_revenue(start_time, end_time)
        response_data = {
            "success": True,
            "total_revenue": result["total_revenue"] or 0,
            "total_orders": result["total_orders"],
            "start_time": start_time.strftime("%H:%M"),
            "end_time": end_time.strftime("%H:%M"),
        }
        return Response(response_data, status=status.HTTP_200_OK)
