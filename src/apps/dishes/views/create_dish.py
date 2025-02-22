from django.urls import reverse_lazy
from django.views.generic import CreateView

from _dishes_examples.forms import DishForm


class DishCreateView(CreateView):
    form_class = DishForm
    template_name = "apps/orders/templates/create.html"
    success_url = reverse_lazy("dishes:list")
