from django.views.generic import UpdateView
from rest_framework.reverse import reverse_lazy

from _dishes_examples.forms import DishForm
from _dishes_examples.models import Dish


class DishUpdateView(UpdateView):
    queryset = Dish.objects.only("title", "slug")  # Debug toolbar
    form_class = DishForm
    context_object_name = "dish"
    template_name = "update.html"
    success_url = reverse_lazy("dishes:list")
