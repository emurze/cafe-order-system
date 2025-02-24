from django.http import HttpResponseNotAllowed, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.orders.models import Order


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("orders:list")

    def get(self, *args, **kwargs) -> HttpResponse:
        return HttpResponseNotAllowed(["POST"])
