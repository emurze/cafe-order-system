from django.views.generic import ListView

from apps.orders.forms import OrderUpdateForm
from apps.orders.models import Order
from config.settings import ORDER_PAGINATE_BY


class OrderListView(ListView):
    queryset = Order.objects.all()
    context_object_name = "orders"
    template_name = "orders/list.html"
    extra_context = {
        "selected": "orders",
        "update_status_form": OrderUpdateForm,
    }
    paginate_by = ORDER_PAGINATE_BY
