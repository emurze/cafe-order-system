from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.orders.models import Order


class OrderDeleteView(DeleteView):
    # TEMPLATE ???
    model = Order
    success_url = reverse_lazy("orders:list")
