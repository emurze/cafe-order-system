from django.views.generic import DetailView

from apps.orders.models import Order


class OrderDetailView(DetailView):
    queryset = Order.objects.all()  # TODO: .only
    context_object_name = "order"
    template_name = "orders/order_detail.html"
    extra_context = {"selected": "orders"}
