from django import forms

from _dishes_examples.models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("title",)
