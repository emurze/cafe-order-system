from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from apps.dishes.forms import DishForm
from apps.dishes.models import Dish


class DishListView(ListView):
    queryset = Dish.objects.only("title", "slug")
    context_object_name = "dishes"
    template_name = "list.html"


class DishDetailView(DetailView):
    queryset = Dish.objects.only("title", "slug")
    context_object_name = "dish"
    template_name = "detail.html"


class DishCreateView(CreateView):
    form_class = DishForm
    template_name = "dishes.html"
    success_url = reverse_lazy("dishes:list")


class DishDeleteView(DeleteView):
    pass


class DishUpdateView(UpdateView):
    pass
