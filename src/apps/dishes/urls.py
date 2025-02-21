from django.urls import path

from apps.dishes.views import (
    DishCreateView,
    DishListView,
    DishDetailView,
    DishDeleteView,
    DishUpdateView,
)

app_name = "dishes"

urlpatterns = [
    path("dishes/", DishListView.as_view(), name="list"),
    path("create/", DishCreateView.as_view(), name="create"),
    path("<slug:slug>/", DishDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", DishUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete", DishDeleteView.as_view(), name="delete"),
]
