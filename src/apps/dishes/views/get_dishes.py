from django.views.generic import ListView

from _dishes_examples.models import Dish


class DishListView(ListView):
    queryset = Dish.objects.only("title", "slug")  # Debug toolbar
    context_object_name = "dishes"
    template_name = "apps/orders/templates/list_orders.html"
    extra_context = {"selected": "dishes"}
