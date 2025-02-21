from django.urls import path

from apps.dishes.views import DishCreateView, DishListView, DishDetailView

app_name = "dishes"

urlpatterns = [
    path("", DishListView.as_view(), name="list"),
    path("create/", DishCreateView.as_view(), name="create"),
    path("<slug:slug>/", DishDetailView.as_view(), name="detail"),
]
