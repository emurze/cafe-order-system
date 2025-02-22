from django.urls import path

from apps.orders.views import create_order, OrderListView
from apps.orders.views.delete_order import OrderDeleteView
from apps.orders.views.get_order import OrderDetailView

app_name = "orders"

urlpatterns = [
    path("", OrderListView.as_view(), name="list"),
    path("create/", create_order, name="create"),
    path("<int:pk>", OrderDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", OrderDeleteView.as_view(), name="delete"),  # ???
]
