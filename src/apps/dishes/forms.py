from django import forms

from apps.dishes.models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("title",)
