from django.urls import path

from apps.orders.api_views.get_order import GetOrderAPIView

app_name = "orders_api"

urlpatterns = [
    path("orders/<int:pk>/", GetOrderAPIView.as_view(), name="detail"),
]
