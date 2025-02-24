from django.views.generic import DetailView

from apps.orders.forms import OrderUpdateForm
from apps.orders.models import Order


class OrderDetailView(DetailView):
    queryset = Order.objects.all()  # TODO: .only
    context_object_name = "order"
    template_name = "orders/detail.html"
    extra_context = {
        "selected": "orders",
    }

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["update_status_form"] = OrderUpdateForm(instance=self.object)
        return context
