from django.views.generic import ListView

from apps.orders.models import Order


class OrderListView(ListView):
    queryset = Order.objects.all()
    context_object_name = "orders"
    template_name = "orders/list_orders.html"
    extra_context = {"selected": "orders"}
