from django.urls import path

from apps.orders.views import (
    create_order,
    OrderListView,
    OrderSearchView,
    OrderDetailView,
    update_order_status,
    get_shift_revenue,
    delete_order,
)

app_name = "orders"

urlpatterns = [
    path("", OrderListView.as_view(), name="list"),
    path("revenue/", get_shift_revenue, name="shift_revenue"),
    path("search/", OrderSearchView.as_view(), name="search"),
    path("create/", create_order, name="create"),
    path("delete/<int:pk>", delete_order, name="delete"),
    path("update/<int:pk>", update_order_status, name="update"),
    path("<int:pk>", OrderDetailView.as_view(), name="detail"),
]
