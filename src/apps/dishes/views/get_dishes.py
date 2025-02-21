from django.views.generic import ListView

from apps.dishes.models import Dish


class DishListView(ListView):
    queryset = Dish.objects.only("title", "slug")  # Debug toolbar
    context_object_name = "dishes"
    template_name = "list.html"
    extra_context = {"selected": "dishes"}
