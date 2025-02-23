from django.views.generic import UpdateView

from apps.orders.forms import OrderUpdateForm
from apps.orders.models import Order


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderUpdateForm
    template_name = "orders/update.html"
    context_object_name = "orders"
    extra_context = {"selected": "orders"}
