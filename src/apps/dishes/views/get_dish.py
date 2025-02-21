from django.views.generic import DetailView

from apps.dishes.models import Dish


class DishDetailView(DetailView):
    queryset = Dish.objects.only("title", "slug")  # Debug toolbar
    context_object_name = "dish"
    template_name = "detail.html"
