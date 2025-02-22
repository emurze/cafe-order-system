from django.views.generic import ListView

from _dishes_examples.models import Dish


class DishListView(ListView):
    queryset = Dish.objects.only("title", "slug")  # Debug toolbar
    context_object_name = "_dishes_examples"
    template_name = "apps/orders/templates/list_orders.html"
    extra_context = {"selected": "_dishes_examples"}
