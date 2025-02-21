from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.dishes.forms import DishForm


class DishCreateView(CreateView):
    form_class = DishForm
    template_name = "create.html"
    success_url = reverse_lazy("dishes:list")
