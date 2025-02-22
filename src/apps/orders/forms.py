from django import forms
from django.forms import modelformset_factory

from apps.orders.models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = (
            "dish",
            "price",
        )


ItemsFormSet = modelformset_factory(
    OrderItem,
    form=OrderItemForm,
    min_num=0,
    fields=("dish", "price"),
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("table_number",)


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("status",)
