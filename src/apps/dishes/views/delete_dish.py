from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.dishes.models import Dish


class DishDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy("dishes:list")
